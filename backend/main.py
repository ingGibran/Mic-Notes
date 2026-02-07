from fastapi import FastAPI

from database import create_db_and_tables
from routers.usuarios import router_usuarios

from contextlib import asynccontextmanager

# Crea la base de datos y las tablas si no existen
@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

# Instancia principal de FastAPI
app = FastAPI(lifespan=lifespan)

# Incluir los routers a la instancia
app.include_router(router_usuarios)
