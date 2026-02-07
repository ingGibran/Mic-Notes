from sqlmodel import SQLModel
from pydantic import field_validator
import re


class crear_usuario_schema(SQLModel):
    username: str
    password: str
    
    @field_validator("password")
    @classmethod
    def validar_password(cls, v: str) -> str:
        if len(v) < 8:
            raise ValueError("La contraseña debe tener al menos 8 caracteres")
        if not re.search(r"\d", v):
            raise ValueError("La contraseña debe incluir al menos un número")
        if not re.search(r"[A-Z]", v):
            raise ValueError("La contraseña debe incluir al menos una mayúscula")
        return v
    
class validar_usuario_schema(SQLModel):
    username: str
    password: str

class leer_usuarios_schema(SQLModel):
    username: str
    password: str