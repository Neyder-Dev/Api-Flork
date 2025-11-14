from sqlalchemy import Column, Integer, String, Date, Boolean, Text
from database import Base
from sqlalchemy.schema import ForeignKey

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    correo = Column(String(100), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    fecha_nacimiento = Column(Date, nullable=True)
    acepta_terminos = Column(Boolean, default=False)

class Receta(Base):
    __tablename__ = "recetas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(150), nullable=False)
    imagen_url = Column(String(255), nullable=False) 
    categoria = Column(String(50), nullable=True)    
    descripcion = Column(Text, nullable=True)

class Favorito(Base):
    __tablename__ = "favoritos"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    receta_id = Column(Integer, ForeignKey("recetas.id"), nullable=False)
    
    