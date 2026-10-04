E-Commerce Backend & Order Management API

A full-stack e-commerce application built with Python, FastAPI, MySQL, HTML, CSS, and JavaScript. The project provides product and customer management, order processing, stock validation, and a browser-based shopping interface connected to a REST API.

🚀 Project Overview

This project demonstrates how to build and connect a FastAPI backend, MySQL database, and browser-based frontend to create an e-commerce order management system.

The backend exposes RESTful API endpoints for managing products, customers, and orders. The frontend provides a simple shopping interface where users can view products, add items to the cart, and place orders.

✨ Features

- Product CRUD operations
- Customer CRUD operations
- Order creation and management
- Product stock validation
- Automatic stock reduction after orders
- Quantity validation
- Product and customer existence validation
- Order total calculation
- MySQL database integration
- RESTful FastAPI APIs
- Swagger API documentation
- CORS support for frontend integration
- Browser-based e-commerce interface
- Shopping cart
- Buy Now functionality
- Order history
- Sales total display
- Responsive and interactive product card

🛠️ Technologies Used

Backend

- Python
- FastAPI
- SQLAlchemy
- Pydantic
- Uvicorn

Database

- MySQL

Frontend

- HTML5
- CSS3
- JavaScript

Development Tools

- PyCharm
- MySQL Community Server
- Git
- GitHub
- Safari Browser

📂 Project Structure

PythonProject4/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
├── README.md
├── .gitignore
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── images/
│       └── Laptop.jpg
│
└── .env

«".env" contains local database configuration and is excluded from GitHub using ".gitignore".»

🗄️ Database

The application uses a MySQL database named:

ecommerce_db

Main tables:

- "products"
- "customers"
- "orders"

Products

Stores product information such as:

- Product ID
- Name
- Description
- Price
- Stock

Customers

Stores customer information such as:

- Customer ID
- Name
- Email
- Phone

Orders

Stores:

- Order ID
- Customer ID
- Product ID
- Quantity
- Total price

⚙️ Setup Instructions

1. Clone the repository

git clone https://github.com/avinashandral123/ecommerce-backend-order-management.git
cd ecommerce-backend-order-management

2. Create a virtual environment

python -m venv .venv

Activate it:

macOS/Linux

source .venv/bin/activate

3. Install dependencies

Install the required Python packages:

pip install fastapi uvicorn sqlalchemy pymysql python-dotenv

4. Configure MySQL

Create the database:

CREATE DATABASE ecommerce_db;

Configure the database connection in a local ".env" file.

Example:

DB_HOST=localhost
DB_PORT=3306
DB_NAME=ecommerce_db
DB_USER=root
DB_PASSWORD=your_password

Do not upload ".env" to GitHub.

5. Run the FastAPI application

python -m uvicorn main:app --reload

The API will run at:

http://127.0.0.1:8000

📖 API Documentation

FastAPI automatically provides interactive Swagger documentation.

Open:

http://127.0.0.1:8000/docs

You can use Swagger to test the API endpoints directly from your browser.

🔗 API Endpoints

Database

Method| Endpoint| Description
GET| "/db-check"| Check database connection

Products

Method| Endpoint| Description
GET| "/products"| Get all products
GET| "/products/{product_id}"| Get a product by ID
POST| "/products"| Create a product
PUT| "/products/{product_id}"| Update a product
DELETE| "/products/{product_id}"| Delete a product

Customers

Method| Endpoint| Description
GET| "/customers"| Get all customers
GET| "/customers/{customer_id}"| Get a customer by ID
POST| "/customers"| Create a customer
PUT| "/customers/{customer_id}"| Update a customer
DELETE| "/customers/{customer_id}"| Delete a customer

Orders

Method| Endpoint| Description
GET| "/orders"| Get all orders
GET| "/orders/{order_id}"| Get an order by ID
POST| "/orders"| Create an order
PUT| "/orders/{order_id}"| Update an order
DELETE| "/orders/{order_id}"| Delete an order

🛒 Frontend

The project also includes a browser-based e-commerce frontend.

Frontend features include:

- Product display
- Product image
- Price and stock display
- Add to Cart
- Buy Now
- Clear Cart
- Place Order
- Cart count
- Cart total
- Order history
- Total sales

The frontend communicates with the FastAPI backend using API requests.

🧪 Validation & Testing

The API was tested using FastAPI Swagger documentation.

Test cases include:

- Successful product creation
- Product update
- Product deletion
- Product not found
- Customer not found
- Invalid order quantity
- Insufficient product stock
- Invalid customer ID
- Invalid product ID
- Successful order creation
- Stock reduction after successful order
- Frontend Buy Now functionality
- Cart functionality
- Order history and sales calculation

📌 Example Order

Example request:

{
  "customer_id": 2,
  "product_id": 1,
  "quantity": 1
}

Example response:

{
  "id": 1,
  "customer_id": 2,
  "product_id": 1,
  "quantity": 1,
  "total_price": 60000
}

🔒 Security

Sensitive database credentials are stored in ".env" and excluded from version control.

The repository uses ".gitignore" to prevent files such as:

.env
.venv/
__pycache__/
*.pyc
.idea/
.DS_Store

🎯 Learning Outcomes

Through this project, I developed practical experience in:

- Python backend development
- FastAPI REST API development
- CRUD operations
- SQL and MySQL database integration
- SQLAlchemy ORM
- API validation using Pydantic
- Exception handling
- Stock and order management
- Frontend and backend integration
- Git and GitHub
- API testing with Swagger
- Building a complete portfolio project

👨‍💻 Author

G. Avinash

B.E. Electronics and Communication Engineering

2026 Graduate

Target Roles

- Python Developer
- Data Analyst

📄 License

This project is created for learning, portfolio, and demonstration purposes.
