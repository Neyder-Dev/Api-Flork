from pydantic import BaseModel, EmailStr
from datetime import date

class UsuarioBase(BaseModel):
    nombre: str
    correo: EmailStr

class UsuarioCreate(UsuarioBase):
    password: str
    fecha_nacimiento: date | None = None
    acepta_terminos: bool = False

class UsuarioLogin(BaseModel):
    correo: EmailStr
    password: str

class UsuarioResponse(UsuarioBase):
    id: int
    fecha_nacimiento: date | None = None
    acepta_terminos: bool

    class Config:
        orm_mode = True
