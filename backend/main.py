from fastapi import FastAPI

from database import create_db_and_tables
from routers.usuarios import router_usuarios

from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(router_usuarios)
