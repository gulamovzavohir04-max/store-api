🛒 E-commerce API
A backend REST API for an e-commerce platform built with Django and Django REST Framework.
The project implements product catalog management, shopping cart functionality, order processing, and JWT authentication.
The API is fully documented with Swagger (OpenAPI).
🚀 Technologies
Python 3
Django
Django REST Framework
JWT Authentication (Simple JWT)
drf-spectacular (Swagger / OpenAPI)
django-filter
SQLite (can be replaced with PostgreSQL)
📦 Features
Authentication
JWT login
JWT token refresh
Get current user profile
Product Catalog
Product categories
Products
Filtering by category
Search products
Sorting
Pagination
Shopping Cart
Add product to cart
Update product quantity
Remove product
Clear cart
Orders
Create order from cart
View user orders
Order details with items
Update order status
Delete order
Admin Panel
Full management via Django Admin:
Users
Categories
Products
Orders
Order Items
📚 API Documentation
Swagger documentation is available at:
http://127.0.0.1:8000/api/docs/
🔑 Authentication
Get access token:
POST /api/token/
Refresh token:
POST /api/token/refresh/
Use token in requests:
Authorization: Bearer <access_token>
📡 Main Endpoints
Accounts

GET /api/accounts/me/
Catalog

GET /api/catalog/categories/
POST /api/catalog/categories/

GET /api/catalog/products/
POST /api/catalog/products/

GET /api/catalog/products/{id}/
PUT /api/catalog/products/{id}/
DELETE /api/catalog/products/{id}/
Cart

GET /api/cart/
POST /api/cart/add/

PATCH /api/cart/update/{item_id}/

DELETE /api/cart/remove/{item_id}/

DELETE /api/cart/clear/
Orders
GET /api/orders/

GET /api/orders/{id}/

POST /api/orders/create/

PATCH /api/orders/{id}/

DELETE /api/orders/{id}/
⚙️ Installation
🐳 Run with Docker
docker compose up --build
1️⃣ Clone repository
git clone https://github.com/yourusername/ecommerce-api.git
cd ecommerce-api
2️⃣ Create virtual environment
python -m venv venv
Activate environment
Windows:
venv\Scripts\activate
Mac / Linux:
source venv/bin/activate
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Run migrations
python manage.py migrate
5️⃣ Create superuser
python manage.py createsuperuser
6️⃣ Start development server
python manage.py runserver
🛠 Admin Panel
Django admin panel is available at:
http://127.0.0.1:8000/admin/
From the admin panel you can manage:
users
products
categories
orders
order items
📄 License
MIT License
👨‍💻 Author
Javohir Gulyamov
Backend project built using Django REST Framework as part of backend development practice.