from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class TareaDB(Base):
    __tablename__ = "tareas"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    descripcion = Column(String, nullable=True)
    completada = Column(Boolean, default=False)