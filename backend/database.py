from sqlmodel import create_engine, SQLModel, Field, Session
from typing import Generator

from datetime import datetime
# Usuarios
class Usuarios(SQLModel, table=True):
    id_usuarios: int | None = Field(default=None, primary_key=True)
    username: str
    hash_password: str

# Notas
class Notas(SQLModel, table=True):
    id_notas: int | None = Field(default=None, primary_key=True)
    titulo: str
    contenido: str
    fecha_registro: datetime = Field(default_factory=datetime.utcnow)
    id_usuario: int | None = Field(default=None, foreign_key="usuarios.id_usuarios")
    
engine = create_engine(
    "sqlite:///database.db", 
    connect_args={"check_same_thread": False}
)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session