from sqlmodel import SQLModel

from datetime import datetime

class crear_nota_schema(SQLModel):
    titulo: str
    contenido: str

class leer_nota_schema(SQLModel):
    id_notas: int
    titulo: str
    contenido: str
    fecha_registro: datetime

class actualizar_nota_schema(SQLModel):
    id_notas: int
    titulo: str
    contenido: str
