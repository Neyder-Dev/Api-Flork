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

@router.get("/populares")
def recetas_populares(db: Session = Depends(database.get_db)):
    """Devuelve 2 recetas aleatorias para la sección de populares."""
    recetas = db.query(models.Receta).order_by(func.rand()).limit(2).all()
    return recetas


@router.get("/recomendadas")
def recetas_recomendadas(db: Session = Depends(database.get_db)):
    """Devuelve 6 recetas aleatorias para la sección de recomendadas."""
    recetas = db.query(models.Receta).order_by(func.rand()).limit(6).all()
    return recetas
