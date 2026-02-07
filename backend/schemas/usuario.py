from sqlmodel import SQLModel


class crear_usuario_schema(SQLModel):
    username: str
    password: str

class validar_usuario_schema(SQLModel):
    username: str
    password: str

class leer_usuarios_schema(SQLModel):
    username: str
    password: str