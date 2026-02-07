from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from database import Notas, Usuarios, get_session
from schemas.notas import crear_nota_schema

router_notas = APIRouter()

@router_notas.post("/notas/", tags=["notas"])
async def crear_nota(nota_data: crear_nota_schema, db: Session = Depends(get_session)):
    
    # Conseguir usuario
    usuario = db.get(Usuarios, nota_data.id_usuario)
    if not usuario:
        raise HTTPException(status_cose=404, detail="Usuario no encontrado")
    
    # Validar esquema
    db_nota = Notas.model_validate(nota_data)
    
    # Guardar nota
    db.add(db_nota)
    db.commit()
    db.refresh(db_nota)
    
    return db_nota