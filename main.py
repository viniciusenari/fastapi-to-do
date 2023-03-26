from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="FastAPI Todo App",
    description="Simple FastAPI Todo App with MongoDB",
    version="0.0.1",
)
app.include_router(router)
