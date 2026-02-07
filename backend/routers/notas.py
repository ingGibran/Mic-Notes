from fastapi import APIRouter, Depends
from sqlmodel import Session

from database import Notas, get_session
from schemas.notas import crear_nota_schema


router_notas = APIRouter()

'''
@router_notas.post("/notas/", tags=["notas"])
async def crear_nota(nota:crear_nota_schema, db: Session = Depends(get_session)):
    db_nota = Notas.model_validate(nota)
    db.add(db_nota)
    db.commit()
    db.refresh(db_nota)
    return nota

@router_notas.get("/notas/", tags=["notas"])
async def leer_notas(id_usuario: int):
'''