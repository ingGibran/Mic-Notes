from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List

from database import Notas, Usuarios, get_session
from schemas.notas import crear_nota_schema


router_notas = APIRouter()


@router_notas.post("/notas/", tags=["notas"])
async def crear_nota(nota_data: crear_nota_schema, db: Session = Depends(get_session)):
    
    # Conseguir usuario
    usuario = db.get(Usuarios, nota_data.id_usuario)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    # Validar esquema
    db_nota = Notas.model_validate(nota_data)
    
    # Guardar nota
    db.add(db_nota)
    db.commit()
    db.refresh(db_nota)
    
    return db_nota

@router_notas.get("/notas/", tags=["notas"], response_model=List[Notas])
async def leer_notas(id_usuario: int, db: Session = Depends(get_session)):

    # Conseguir usuario
    usuario = db.get(Usuarios, id_usuario)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    # Consultar notas
    statement = select(Notas).where(Notas.id_usuario == id_usuario)
    notas_db = db.exec(statement).all()
    
    # Regresar notas
    return notas_db