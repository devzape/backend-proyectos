from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel, ConfigDict
from sqlalchemy.orm import Session
import models
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

class TareaCreate(BaseModel):
    titulo: str
    descripcion: str | None = None
    completada: bool = False

class TareaResponse(TareaCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# NUEVO: Endpoint de listar tareas con filtros y paginación
@app.get("/tareas", response_model=list[TareaResponse])
def obtener_tareas(
    completada: bool | None = None,
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    query = db.query(models.TareaDB)
    
    # Si pasan el parámetro 'completada', filtramos
    if completada is not None:
        query = query.filter(models.TareaDB.completada == completada)
        
    tareas = query.offset(skip).limit(limit).all()
    return tareas

@app.post("/tareas", response_model=TareaResponse, status_code=status.HTTP_201_CREATED)
def crear_tarea(tarea: TareaCreate, db: Session = Depends(get_db)):
    nueva_tarea = models.TareaDB(**tarea.model_dump())
    db.add(nueva_tarea)
    db.commit()
    db.refresh(nueva_tarea)
    return nueva_tarea

@app.get("/tareas/{tarea_id}", response_model=TareaResponse)
def obtener_tarea(tarea_id: int, db: Session = Depends(get_db)):
    tarea = db.query(models.TareaDB).filter(models.TareaDB.id == tarea_id).first()
    if not tarea:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"La tarea con el ID {tarea_id} no existe."
        )
    return tarea

@app.put("/tareas/{tarea_id}", response_model=TareaResponse)
def actualizar_tarea(tarea_id: int, tarea_actualizada: TareaCreate, db: Session = Depends(get_db)):
    tarea_query = db.query(models.TareaDB).filter(models.TareaDB.id == tarea_id)
    tarea = tarea_query.first()
    
    if not tarea:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"La tarea con el ID {tarea_id} no existe."
        )
    
    tarea_query.update(tarea_actualizada.model_dump(), synchronize_session=False)
    db.commit()
    return tarea_query.first()

@app.delete("/tareas/{tarea_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_tarea(tarea_id: int, db: Session = Depends(get_db)):
    tarea = db.query(models.TareaDB).filter(models.TareaDB.id == tarea_id).first()
    
    if not tarea:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"La tarea con el ID {tarea_id} no existe."
        )
    
    db.delete(tarea)
    db.commit()
    return None