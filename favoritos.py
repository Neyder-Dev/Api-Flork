from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import database, models

router = APIRouter(prefix="/favoritos", tags=["Favoritos"])

@router.post("/agregar")
def agregar_favorito(usuario_id: int, receta_id: int, db: Session = Depends(database.get_db)):

    existe = db.query(models.Favorito).filter_by(usuario_id=usuario_id, receta_id=receta_id).first()
    if existe:
        raise HTTPException(status_code=400, detail="La receta ya está en favoritos")

    nuevo = models.Favorito(usuario_id=usuario_id, receta_id=receta_id)
    db.add(nuevo)
    db.commit()
    return {"message": "Receta agregada a favoritos ✅"}

@router.delete("/eliminar")
def eliminar_favorito(usuario_id: int, receta_id: int, db: Session = Depends(database.get_db)):
    favorito = db.query(models.Favorito).filter_by(usuario_id=usuario_id, receta_id=receta_id).first()

    if not favorito:
        raise HTTPException(status_code=404, detail="No está en favoritos")

    db.delete(favorito)
    db.commit()
    return {"message": "Receta eliminada de favoritos ❌"}

@router.get("/usuario/{usuario_id}")
def favoritos_usuario(usuario_id: int, db: Session = Depends(database.get_db)):
    favoritos = db.query(models.Receta) \
                  .join(models.Favorito, models.Receta.id == models.Favorito.receta_id) \
                  .filter(models.Favorito.usuario_id == usuario_id) \
                  .all()
    return favoritos


