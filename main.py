from fastapi import FastAPI
from routes.r0931795_endpoints import router

app = FastAPI()

app.include_router(router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Welcome to the API"}

