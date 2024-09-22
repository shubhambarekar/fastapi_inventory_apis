from sqlalchemy.orm import Session
from models.data import Products
from schemas import data
from fastapi import HTTPException,status
import sqlalchemy

def get_all(db :Session):
    return db.query(Products).all()

def check_product(name:str,db: Session):
    detail = db.query(Products).filter(Products.name == name).first()   
    if not detail:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"product with '{name}' not found")
    return detail

def buy_product(name:str,request : data.BuyProducts,db: Session):
    detail = db.query(Products).filter(Products.name == name).first()
    if not detail:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"product with '{name}' not found")
    print(detail.quantity)
    detail.quantity = detail.quantity - request.quantity
    db.commit()
    return f'order placed, The total amount will be {request.quantity*detail.price}'

def update_product_inventory(name:str,request : data.BuyProducts,db: Session):
    detail = db.query(Products).filter(Products.name == name).first()
    if not detail:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"product with '{name}' not found")
    detail.quantity = detail.quantity + request.quantity
    db.commit()
    return f'Inventory updated, The total quantity will be {detail.quantity}'

def add_products(request : data.Products,db: Session):
    new_product = Products(name=request.product_name,price=request.price,quantity=request.quantity)
    try:
        db.add(new_product)
        db.commit()
        db.refresh(new_product)
        return f"The product with '{request.product_name}' added sucessfully."
    except sqlalchemy.exc.IntegrityError:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                            detail=f"Product with '{request.product_name}' name already exist")

def update_price(id:int,request : data.Products,db: Session):
    edit_product = db.query(Products).filter(Products.id == id).first()
    
    if not edit_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"product with id '{id}' not found")
    
    # Update the fields of the SQLAlchemy object
    for key, value in dict(request).items():
        setattr(edit_product, key, value)

    db.commit()
    return f"The product with '{id}' updated sucessfully."

def destroy(id:int,db: Session):
    blog = db.query(Products).filter(Products.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"product with id '{id}' not found")

    blog.delete(synchronize_session=False)
    db.commit()
    return f"The product with '{id}' deleted sucessfully."