from pydantic import BaseModel

class ProductsUser(BaseModel):
    product_name: str
    # price: float
    quantity: int
    class Config():
        orm_mode = True

class Products(BaseModel):
    product_name: str
    price: float
    quantity: int
    class Config():
        orm_mode = True

class BuyProducts(BaseModel):
    # product_name: str
    quantity: int
    class Config():
        orm_mode = True