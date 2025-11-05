from sqlalchemy import Column, Integer, String, Date, Boolean
from .database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    correo = Column(String(100), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    fecha_nacimiento = Column(Date, nullable=True)
    acepta_terminos = Column(Boolean, default=False)
