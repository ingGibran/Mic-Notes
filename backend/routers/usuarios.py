from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from typing import List

from database import Usuarios, get_session
from schemas.usuario import crear_usuario_schema, leer_usuarios_schema


router_usuarios = APIRouter()

@router_usuarios.post("/usuarios/", tags=["usuarios"])
async def crear_usuario(usuario:crear_usuario_schema, db: Session = Depends(get_session)):
    db_usuario = Usuarios.model_validate(usuario)
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return usuario

@router_usuarios.get("/usuarios/", tags=["usuarios"], response_model=List[leer_usuarios_schema])
async def leer_usuarios(db: Session = Depends(get_session)):
    usuarios = db.exec(select(Usuarios)).all()
    return usuarios

