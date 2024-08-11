from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.r0931795_endpoints import router as router

app = FastAPI(docs_url=None)


app.include_router(router)
