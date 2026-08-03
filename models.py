from pydantic import BaseModel
from typing import Optional
from sqlalchemy import Column, Integer, String, Boolean
from database import Base

# Lo que recibimos cuando alguien crea una tarea
class TareaCreate(BaseModel):
    titulo: str
    descripcion: Optional[str] = None
    completada: bool = False

# Lo que recibimos cuando actualizamos una tarea (método PUT)
class TareaUpdate(BaseModel):
    titulo: Optional[str] = None
    descripcion: Optional[str] = None
    completada: Optional[bool] = None

# Lo que devolvemos (incluye el ID generado)
class Tarea(BaseModel):
    id: int
    titulo: str
    descripcion: Optional[str] = None
    completada: bool = False

# Modelo de la tabla para la Base de Datos
class TareaDB(Base):
    __tablename__ = "tareas"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    descripcion = Column(String, nullable=True)
    completada = Column(Boolean, default=False)