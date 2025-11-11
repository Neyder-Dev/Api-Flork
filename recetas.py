from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import database, models, schemas

router = APIRouter(prefix="/recetas", tags=["Recetas"])

@router.get("/", response_model=list[schemas.RecetaResponse])
def obtener_recetas(db: Session = Depends(database.get_db)):
    return db.query(models.Receta).all()
