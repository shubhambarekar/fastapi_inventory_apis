from fastapi import APIRouter
from schemas import data
from fastapi import Depends,status
from sqlalchemy.orm import Session
from config import database
from repository import products

postdata = APIRouter(
    prefix="/admin", 
    tags=['admin'])

conn = database.conn

@postdata.get("/all_products")
async def show_all(db: Session = Depends(conn)):
    return products.get_all(db)

@postdata.get("/product/{name}")
async def show_product(name,db: Session = Depends(conn)):
    return products.check_product(name,db)

@postdata.post("/add_new_product")
async def add_product(request: data.Products,db: Session = Depends(conn)):
    return products.add_products(request,db)

@postdata.put("/edit/{id}")
async def edit_product(id,request : data.Products ,db: Session = Depends(conn)):
    return products.update_price(id,request,db)

@postdata.delete("/delete/{id}")
async def delete_product(id,db: Session = Depends(conn)):
    return products.destroy(id,db)

# @postdata.put("/buy/{name}")
# async def buy_product(name,request : data.BuyProducts, db: Session = Depends(conn)):
#     return products.buy_product(name,request,db)

@postdata.put("/inventory/{name}")
async def update_inventory(name,request : data.BuyProducts, db: Session = Depends(conn)):
    return products.update_product_inventory(name,request,db)