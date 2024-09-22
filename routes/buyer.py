from fastapi import APIRouter
from schemas import data
from fastapi import Depends,status
from sqlalchemy.orm import Session
from config import database
from repository import products

buyer = APIRouter(
    prefix="/user", 
    tags=['user'])

conn = database.conn

@buyer.put("/{name}")
async def buy_product(name,request : data.BuyProducts, db: Session = Depends(conn)):
    return products.buy_product(name,request,db)