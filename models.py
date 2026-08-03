from pydantic import BaseModel
from typing import Optional

# Lo que ya tenías para crear
class TareaCreate(BaseModel):
    titulo: str
    descripcion: Optional[str] = None
    completada: bool = False

# NUEVO: Esquema para actualizar (permite modificar solo lo que haga falta)
class TareaUpdate(BaseModel):
    titulo: Optional[str] = None
    descripcion: Optional[str] = None
    completada: Optional[bool] = None

# Lo que devuelve la API
class TareaResponse(BaseModel):
    id: int
    titulo: str
    descripcion: Optional[str] = None
    completada: bool

    class Config:
        from_attributes = True