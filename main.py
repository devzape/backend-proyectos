from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
import models
import database

# Crea las tablas en la base de datos si no existen (Corregido)
database.Base.metadata.create_all(bind=database.engine)

app = FastAPI(
    title="API de Tareas Pro",
    version="2.0",
    description="Backend avanzado con FastAPI, SQLAlchemy y manejo de errores."
)

# Dependencia para obtener la sesión de base de datos por cada request
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 1. OBTENER TODAS LAS TAREAS
@app.get("/tareas", response_model=list[models.TareaResponse])
def obtener_tareas(db: Session = Depends(get_db)):
    tareas = db.query(models.TareaDB).all()
    return tareas

# 2. CREAR TAREA
@app.post("/tareas", response_model=models.TareaResponse, status_code=status.HTTP_201_CREATED)
def crear_tarea(tarea: models.TareaCreate, db: Session = Depends(get_db)):
    nueva_tarea = models.TareaDB(
        titulo=tarea.titulo,
        descripcion=tarea.descripcion,
        completada=tarea.completada
    )
    db.add(nueva_tarea)
    db.commit()
    db.refresh(nueva_tarea)
    return nueva_tarea

# 3. OBTENER UNA TAREA POR ID (Con manejo de error 404)
@app.get("/tareas/{tarea_id}", response_model=models.TareaResponse)
def obtener_tarea(tarea_id: int, db: Session = Depends(get_db)):
    tarea = db.query(models.TareaDB).filter(models.TareaDB.id == tarea_id).first()
    if not tarea:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"La tarea con el ID {tarea_id} no existe."
        )
    return tarea

# 4. ACTUALIZAR TAREA (PUT)
@app.put("/tareas/{tarea_id}", response_model=models.TareaResponse)
def actualizar_tarea(tarea_id: int, tarea_actualizada: models.TareaUpdate, db: Session = Depends(get_db)):
    tarea = db.query(models.TareaDB).filter(models.TareaDB.id == tarea_id).first()
    
    if not tarea:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No se puede actualizar: La tarea con el ID {tarea_id} no existe."
        )
    
    # Actualizamos solo los campos que el usuario envió
    datos_dict = tarea_actualizada.model_dump(exclude_unset=True)
    for clave, valor in datos_dict.items():
        setattr(tarea, clave, valor)
    
    db.commit()
    db.refresh(tarea)
    return tarea

# 5. ELIMINAR TAREA (DELETE)
@app.delete("/tareas/{tarea_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_tarea(tarea_id: int, db: Session = Depends(get_db)):
    tarea = db.query(models.TareaDB).filter(models.TareaDB.id == tarea_id).first()
    
    if not tarea:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No se puede eliminar: La tarea con el ID {tarea_id} no existe."
        )
    
    db.delete(tarea)
    db.commit()
    return None