from fastapi import FastAPI
from routes.data import postdata
from routes.buyer import buyer
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.include_router(postdata)
app.include_router(buyer)