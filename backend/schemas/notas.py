from sqlmodel import SQLModel
from datetime import datetime


class crear_nota_schema(SQLModel):
    titulo: str
    contenido: str
    id_usuario: int

class actualizar_nota_schema(SQLModel):
    id: int
    titulo: str
    contenido: str
