from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List

from database import Usuarios, get_session
from schemas.usuario import crear_usuario_schema, leer_usuarios_schema, validar_usuario_schema
from security import hash_password, verify_password


router_usuarios = APIRouter()

@router_usuarios.post("/usuarios/crear", tags=["usuarios"])
async def crear_usuario(usuario:crear_usuario_schema, db: Session = Depends(get_session)):
    # Hashear contraseña
    db_usuario = Usuarios.model_validate(usuario)
    hashed_password = hash_password(db_usuario.password)
    db_usuario.password = hashed_password
    
    # Agregar usuario
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return usuario

@router_usuarios.post("/usuarios/iniciar_sesion", tags=["usuarios"])
async def login(usuario_login: validar_usuario_schema, db: Session = Depends(get_session)):
    # Buscar usuario
    statement = select(Usuarios).where(Usuarios.username == usuario_login.username)
    usuario_db = db.exec(statement).first()
    
    # Verificar que existe usuario
    if not usuario_db:
        raise HTTPException(status_code=400, detail="Usuario o contraseña incorrectos")
    
    # Validar contraseñas
    es_valida = verify_password(usuario_login.password, usuario_db.password)
    
    # Regresar estado
    if not es_valida:
        raise HTTPException(status_code=400, detail="Usuario o contraseña incorrectos")
    
    return {"message": "Inicio de sesión exitoso", "user_id": usuario_db.id_usuarios}
    
    
@router_usuarios.get("/usuarios/", tags=["usuarios"], response_model=List[leer_usuarios_schema])
async def leer_usuarios(db: Session = Depends(get_session)):
    usuarios = db.exec(select(Usuarios)).all()
    return usuarios

