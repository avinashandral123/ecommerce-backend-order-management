from pydantic import BaseModel, Field


class ProductCreate(BaseModel):
    name: str
    description: str | None = None
    price: float
    stock: int


class CustomerCreate(BaseModel):
    name: str
    email: str
    phone: str | None = None


class OrderCreate(BaseModel):
    customer_id: int
    product_id: int
    quantity: int = Field(gt=0)


class OrderUpdate(BaseModel):
    quantity: int = Field(gt=0)




