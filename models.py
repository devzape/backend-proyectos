from sqlalchemy import Column, Integer, String, Boolean
from pydantic import BaseModel, ConfigDict
from typing import Optional
from database import Base

# ==========================================
# MODELO ORM (SQLAlchemy - Tabla en BD)
# ==========================================
class TareaDB(Base):
    __tablename__ = "tareas"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    descripcion = Column(String, nullable=True)
    completada = Column(Boolean, default=False)


# ==========================================
# ESQUEMAS PYDANTIC (Validación de API)
# ==========================================
class TareaCreate(BaseModel):
    titulo: str
    descripcion: Optional[str] = None
    completada: bool = False

class TareaUpdate(BaseModel):
    titulo: Optional[str] = None
    descripcion: Optional[str] = None
    completada: Optional[bool] = None

class TareaResponse(BaseModel):
    id: int
    titulo: str
    descripcion: Optional[str] = None
    completada: bool

    model_config = ConfigDict(from_attributes=True)