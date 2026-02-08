from fastapi import FastAPI

from database import create_db_and_tables
from routers.usuarios import router_usuarios
from routers.notas import router_notas
from routers.transcribe import transcribe_router

from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

# Crea la base de datos y las tablas si no existen
@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

# Instancia principal de FastAPI
app = FastAPI(lifespan=lifespan)

# Configurar CORS
origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir los routers a la instancia
app.include_router(router_usuarios)
app.include_router(router_notas)
app.include_router(transcribe_router)