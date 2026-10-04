from fastapi import FastAPI, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from database import test_database_connection, engine, Base, SessionLocal
import models
from schemas import ProductCreate, CustomerCreate, OrderCreate, OrderUpdate
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.mount("/frontend", StaticFiles(directory="frontend",html= True), name="frontend")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {"message": "E-commerce API is running"}


@app.get("/db-check")
def db_check():
    try:
        result = test_database_connection()
        return {
            "message": "Database connected successfully!",
            "test_result": result
        }
    except Exception as e:
        return {
            "message": "Database connection failed",
            "error": str(e)
        }


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/products")
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db)
):
    new_product = models.Product(
        name=product.name,
        description=product.description,
        price=product.price,
        stock=product.stock
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product


@app.get("/products")
def get_products(db: Session = Depends(get_db)):
    products = db.query(models.Product).all()
    return products


@app.get("/products/{product_id}")
def get_product(
    product_id: int,
    db: Session = Depends(get_db)
):
    product = db.query(models.Product).filter(
        models.Product.id == product_id
    ).first()

    if not product:
       raise HTTPException(status_code=404, detail="Product not found")
    return product


@app.put("/products/{product_id}")
def update_product(
    product_id: int,
    product: ProductCreate,
    db: Session = Depends(get_db)
):
    existing_product = db.query(models.Product).filter(
        models.Product.id == product_id
    ).first()

    if existing_product is None:
        return {"message": "Product not found"}

    existing_product.name = product.name
    existing_product.description = product.description
    existing_product.price = product.price
    existing_product.stock = product.stock

    db.commit()
    db.refresh(existing_product)

    return existing_product


@app.delete("/products/{product_id}")
def delete_product(
    product_id: int,
    db: Session = Depends(get_db)
):
    product = db.query(models.Product).filter(
        models.Product.id == product_id
    ).first()

    if product is None:
        return {"message": "Product not found"}

    db.delete(product)
    db.commit()

    return {
        "message": "Product deleted successfully",
        "product_id": product_id
    }
@app.post("/customers")
def create_customer(
    customer: CustomerCreate,
    db: Session = Depends(get_db)
):
    new_customer = models.Customer(
        name=customer.name,
        email=customer.email,
        phone=customer.phone
    )

    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)

    return new_customer
@app.get("/customers")
def get_customers(db: Session = Depends(get_db)):
    customers = db.query(models.Customer).all()
    return customers

@app.get("/customers/{customer_id}")
def get_customer(
            customer_id: int,
            db: Session = Depends(get_db)
    ):
        customer = db.query(models.Customer).filter(
            models.Customer.id == customer_id
        ).first()

        if customer is None:
            raise HTTPException(
                status_code=404,
                detail="Customer not found"
            )

        return customer


@app.put("/customers/{customer_id}")
def update_customer(
    customer_id: int,
    customer: CustomerCreate,
    db: Session = Depends(get_db)
):
    existing_customer = db.query(models.Customer).filter(
        models.Customer.id == customer_id
    ).first()

    if existing_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    existing_customer.name = customer.name
    existing_customer.email = customer.email
    existing_customer.phone = customer.phone

    db.commit()
    db.refresh(existing_customer)

    return existing_customer
@app.delete("/customers/{customer_id}")
def delete_customer(
    customer_id: int,
    db: Session = Depends(get_db)
):
    customer = db.query(models.Customer).filter(
        models.Customer.id == customer_id
    ).first()

    if customer is None:
         raise HTTPException(status_code=404, detail="Customer not found")

    db.delete(customer)
    db.commit()

    return {
        "message": "Customer deleted successfully",
        "customer_id": customer_id
    }
@app.post("/orders")
def create_order(
    order: OrderCreate,
    db: Session = Depends(get_db)
):
    product = db.query(models.Product).filter(
        models.Product.id == order.product_id
    ).first()

    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    if order.quantity>product.stock:
        raise HTTPException(status_code=400, detail="insufficient stock")
        return {"message": "insufficient stock"}

    customer = db.query(models.Customer).filter(
        models.Customer.id == order.customer_id
    ).first()

    if customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")

    total_price = product.price * order.quantity
    product.stock-=order.quantity

    new_order = models.Order(
        customer_id=order.customer_id,
        product_id=order.product_id,
        quantity=order.quantity,
        total_price=total_price
    )

    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    return new_order
@app.get("/orders")
def get_orders(db: Session = Depends(get_db)):
    orders = db.query(models.Order).all()
    return orders
@app.get("/orders/{order_id}")
def get_order(
    order_id: int,
    db: Session = Depends(get_db)
):
    order = db.query(models.Order).filter(
        models.Order.id == order_id
    ).first()

    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")

    return order

@app.put("/orders/{order_id}")
def update_order(
    order_id: int,
    order: OrderUpdate,
    db: Session = Depends(get_db)
):
    existing_order = db.query(models.Order).filter(
        models.Order.id == order_id
    ).first()

    if existing_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    product = db.query(models.Product).filter(
        models.Product.id == existing_order.product_id
    ).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    if order.quantity<=0:
        raise HTTPException(status_code=400, detail="quantity must be greater than zero")
    difference = order.quantity-existing_order.quantity
    if difference>product.stock:
        raise HTTPException(status_code=400, detail="insufficient stock")
    product.stock-=difference
    existing_order.quantity=order.quantity
    existing_order.total_price= product.price * order.quantity

    db.commit()
    db.refresh(existing_order)

    return existing_order
@app.delete("/orders/{order_id}")
def delete_order(
    order_id: int,
    db: Session = Depends(get_db)
):
    existing_order = db.query(models.Order).filter(
        models.Order.id == order_id
    ).first()

    if existing_order is None:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    product = db.query(models.Product).filter(
        models.Product.id == existing_order.product_id
    ).first()

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    product.stock += existing_order.quantity

    db.delete(existing_order)
    db.commit()

    return {
        "message": "Order deleted successfully"
    }