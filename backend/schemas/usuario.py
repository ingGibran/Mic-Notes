from sqlmodel import SQLModel


class crear_usuario_schema(SQLModel):
    username: str
    hash_password: str

class leer_usuarios_schema(SQLModel):
    username: str