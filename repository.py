from sqlalchemy.orm import Session
from . import models
from .security import hash_password, verify_password

def crear_usuario(db: Session, nombre: str, correo: str, password: str, fecha_nacimiento=None, acepta_terminos=False):
    existente = db.query(models.Usuario).filter(models.Usuario.correo == correo).first()
    if existente:
        return None  

    usuario = models.Usuario(
        nombre=nombre,
        correo=correo,
        password=hash_password(password),
        fecha_nacimiento=fecha_nacimiento,
        acepta_terminos=acepta_terminos
    )

    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return usuario


def autenticar_usuario(db: Session, correo: str, password: str):
    usuario = db.query(models.Usuario).filter(models.Usuario.correo == correo).first()
    if not usuario:
        return None

    if not verify_password(password, usuario.password):
        return None

    return usuario
