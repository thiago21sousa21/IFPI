from fastapi import FastAPI, HTTPException, status
from ulid import ulid
from routes_cidades import router

app = FastAPI()
app.include_router(router, prefix="/cidades")

