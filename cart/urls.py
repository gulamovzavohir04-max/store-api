from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CartViewSet
from .views import CartUpdateView
from .views import CartRemoveView
router = DefaultRouter()
router.register(r"", CartViewSet, basename="cart")

urlpatterns = [
    path("", include(router.urls)),
    path("update/", CartUpdateView.as_view(), name="cart_update"),
     path("remove/", CartRemoveView.as_view(), name="cart_remove"),
]