from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Cart, CartItem
from .serializers import CartSerializer, AddToCartSerializer, UpdateCartItemSerializer
from catalog.models import Product

from rest_framework.views import APIView
from rest_framework import status


class CartRemoveView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        product_id = request.data.get("product_id")

        if product_id is None:
            return Response({"detail": "product_id is required."}, status=400)

        cart, _ = Cart.objects.get_or_create(user=request.user)

        deleted, _ = CartItem.objects.filter(cart=cart, product_id=product_id).delete()
        if deleted == 0:
            return Response({"detail": "Item not found in cart."}, status=404)

        return Response({"detail": "Item deleted."}, status=200)


class CartUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request):
        product_id = request.data.get("product_id")
        quantity = request.data.get("quantity")

        if product_id is None or quantity is None:
            return Response({"detail": "product_id and quantity are required."}, status=400)

        try:
            quantity = int(quantity)
        except ValueError:
            return Response({"detail": "quantity must be an integer."}, status=400)

        if quantity < 0:
            return Response({"detail": "quantity must be >= 0."}, status=400)

        cart, _ = Cart.objects.get_or_create(user=request.user)

        try:
            item = CartItem.objects.get(cart=cart, product_id=product_id)
        except CartItem.DoesNotExist:
            return Response({"detail": "Item not found in cart."}, status=404)

        # Если quantity = 0 — удаляем item
        if quantity == 0:
            item.delete()
            return Response({"detail": "Item removed."}, status=200)

        item.quantity = quantity
        item.save()

        return Response({"detail": "Quantity updated.", "product_id": product_id, "quantity": quantity}, status=200)
class CartViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def _get_cart(self, user):
        cart, _ = Cart.objects.get_or_create(user=user)
        return cart

    def list(self, request):
        cart = self._get_cart(request.user)
        return Response(CartSerializer(cart).data)

    @action(detail=False, methods=["post"], url_path="add")
    def add(self, request):
        cart = self._get_cart(request.user)
        s = AddToCartSerializer(data=request.data)
        s.is_valid(raise_exception=True)

        product = Product.objects.get(id=s.validated_data["product_id"])
        qty = s.validated_data.get("quantity", 1)

        item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        item.quantity = item.quantity + qty if not created else qty
        item.save()

        return Response(CartSerializer(cart).data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["patch"], url_path=r"update/(?P<item_id>\d+)")
    def update_item(self, request, item_id=None):
        cart = self._get_cart(request.user)
        s = UpdateCartItemSerializer(data=request.data)
        s.is_valid(raise_exception=True)

        try:
            item = CartItem.objects.get(id=item_id, cart=cart)
        except CartItem.DoesNotExist:
            return Response({"detail": "Item not found"}, status=404)

        item.quantity = s.validated_data["quantity"]
        item.save()
        return Response(CartSerializer(cart).data)

    @action(detail=False, methods=["delete"], url_path=r"remove/(?P<item_id>\d+)")
    def remove(self, request, item_id=None):
        cart = self._get_cart(request.user)
        CartItem.objects.filter(id=item_id, cart=cart).delete()
        return Response(CartSerializer(cart).data)

    @action(detail=False, methods=["delete"], url_path="clear")
    def clear(self, request):
        cart = self._get_cart(request.user)
        cart.items.all().delete()
        return Response(CartSerializer(cart).data)
    