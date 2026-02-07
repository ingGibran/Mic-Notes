from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List

from database import Notas, Usuarios, get_session
from schemas.notas import crear_nota_schema, actualizar_nota_schema


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


@router_notas.delete("/notas/", tags=["notas"])
async def eliminar_nota(id_nota: int, db: Session = Depends(get_session)):
    
    # Buscar nota
    nota_db = db.get(Notas, id_nota)
    if not nota_db:
        raise HTTPException(status_code=404, detail="Nota no encontrada")
    
    # Eliminar nota
    db.delete(nota_db)
    db.commit()
    
    return {"mensaje": f"nota {nota_db.id} eliminada con exito"}


@router_notas.patch("/notas/", tags=["notas"])
async def actualizar_nota(nota: actualizar_nota_schema, db: Session = Depends(get_session)):
    
    # Buscar nota
    nota_db = db.get(Notas, nota.id)
    if not nota_db:
        raise HTTPException(status_code=404, detail="Nota no encontrada")
    
    # Actualizar datos
    nota_db.titulo = nota.titulo
    nota_db.contenido = nota.contenido
    
    # Actualizar nota
    db.add(nota_db)
    db.commit()
    db.refresh(nota_db)
    
    return {"mensaje": f"nota {nota_db.id} actualizada con exito", "nota": nota_db}