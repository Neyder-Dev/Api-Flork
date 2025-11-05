from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import schemas, database
from . import repository as usuario_repo


router = APIRouter(prefix="/auth", tags=["Autenticación"])

@router.post("/registro", response_model=schemas.UsuarioResponse)
def registrar_usuario(request: schemas.UsuarioCreate, db: Session = Depends(database.get_db)):
    usuario = usuario_repo.crear_usuario(
        db,
        nombre=request.nombre,
        correo=request.correo,
        password=request.password,
        fecha_nacimiento=request.fecha_nacimiento,
        acepta_terminos=request.acepta_terminos
    )
    if not usuario:
        raise HTTPException(status_code=400, detail="El correo ya está registrado")
    return usuario


@router.post("/login")
def login(request: schemas.UsuarioLogin, db: Session = Depends(database.get_db)):
    usuario = usuario_repo.autenticar_usuario(db, request.correo, request.password)
    if not usuario:
        raise HTTPException(status_code=401, detail="Correo o contraseña incorrectos")
    return {"mensaje": "Login exitoso", "usuario": usuario.correo}
