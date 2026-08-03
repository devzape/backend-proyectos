from pydantic import BaseModel
from typing import Optional

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
    completada: bool