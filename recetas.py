from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
import database, models, schemas

router = APIRouter(prefix="/recetas", tags=["Recetas"])

@router.get("/", response_model=list[schemas.RecetaResponse])
def obtener_recetas(categoria: str | None = None, db: Session = Depends(database.get_db)):
    query = db.query(models.Receta)

    if categoria:
        query = query.filter(func.lower(models.Receta.categoria) == categoria.lower())

    return query.all()
