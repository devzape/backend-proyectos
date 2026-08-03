from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

import models
from database import engine, get_db

# Creamos las tablas en la base de datos automáticamente al iniciar
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="API de Tareas con Base de Datos")

# 1. CREAR TAREA (POST)
@app.post("/tareas", response_model=models.Tarea, status_code=status.HTTP_201_CREATED)
def crear_tarea(tarea: models.TareaCreate, db: Session = Depends(get_db)):
    # Creamos una instancia del modelo de base de datos con los datos que llegan
    nueva_tarea = models.TareaDB(
        titulo=tarea.titulo,
        descripcion=tarea.descripcion,
        completada=tarea.completada
    )
    db.add(nueva_tarea)
    db.commit()
    db.refresh(nueva_tarea) # Actualiza la variable para obtener el ID generado por la DB
    return nueva_tarea

# 2. OBTENER TODAS LAS TAREAS (GET)
@app.get("/tareas", response_model=List[models.Tarea])
def obtener_tareas(db: Session = Depends(get_db)):
    tareas = db.query(models.TareaDB).all()
    return tareas

# 3. OBTENER UNA TAREA POR ID (GET)
@app.get("/tareas/{id}", response_model=models.Tarea)
def obtener_tarea(id: int, db: Session = Depends(get_db)):
    tarea = db.query(models.TareaDB).filter(models.TareaDB.id == id).first()
    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return tarea

# 4. ACTUALIZAR TAREA (PUT)
@app.put("/tareas/{id}", response_model=models.Tarea)
def actualizar_tarea(id: int, tarea_actualizada: models.TareaUpdate, db: Session = Depends(get_db)):
    tarea_query = db.query(models.TareaDB).filter(models.TareaDB.id == id)
    tarea_db = tarea_query.first()
    
    if not tarea_db:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    
    # Solo actualizamos los campos que el usuario envió (si no son None)
    datos_actualizacion = tarea_actualizada.dict(exclude_unset=True)
    tarea_query.update(datos_actualizacion, synchronize_session=False)
    
    db.commit()
    return tarea_query.first()

# 5. BORRAR TAREA (DELETE)
@app.delete("/tareas/{id}", status_code=status.HTTP_204_NO_CONTENT)
def borrar_tarea(id: int, db: Session = Depends(get_db)):
    tarea = db.query(models.TareaDB).filter(models.TareaDB.id == id).first()
    
    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    
    db.delete(tarea)
    db.commit()
    return None