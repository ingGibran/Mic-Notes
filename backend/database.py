from sqlmodel import create_engine, SQLModel, Field, Session, Relationship
from typing import Generator, Optional, List

from datetime import datetime

# Usuarios
class Usuarios(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    password: str

    notas: List["Notas"] = Relationship(back_populates="usuario")
    
    
# Notas
class Notas(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    titulo: str
    contenido: str
    fecha_registro: datetime = Field(default_factory=datetime.utcnow)
    
    id_usuario: int = Field(foreign_key="usuarios.id")
    
    usuario: Optional[Usuarios] = Relationship(back_populates="notas")
    
    
engine = create_engine(
    "sqlite:///database.db", 
    connect_args={"check_same_thread": False}
)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session