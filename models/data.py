from sqlalchemy import Column,String,Integer,ForeignKey,Float,table
from sqlalchemy.orm import relationship
from config.database import Base

class Products(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Float)
    quantity = Column(Integer)

