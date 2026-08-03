from fastapi import FastAPI, HTTPException
from typing import List
from models import Tarea, TareaCreate, TareaUpdate

app = FastAPI(
    title="API de Gestión de Tareas Pro",
    description="Backend profesional con FastAPI para arrancar el GitHub a todo ojete.",
    version="1.0.0"
)

# "Base de datos" temporal en memoria
db_tareas: List[Tarea] = []
contador_id = 1

@app.get("/", tags=["General"])
def inicio():
    return {"mensaje": "Backend activo y funcionando a pleno 🚀"}

# GET: Obtener todas las tareas
@app.get("/tareas", response_model=List[Tarea], tags=["Tareas"])
def obtener_tareas():
    return db_tareas

# POST: Crear una nueva tarea
@app.post("/tareas", response_model=Tarea, status_code=201, tags=["Tareas"])
def crear_tarea(tarea_in: TareaCreate):
    global contador_id
    nueva_tarea = Tarea(
        id=contador_id,
        titulo=tarea_in.titulo,
        descripcion=tarea_in.descripcion,
        completada=tarea_in.completada
    )
    db_tareas.append(nueva_tarea)
    contador_id += 1
    return nueva_tarea

# PUT: Actualizar una tarea existente por ID
@app.put("/tareas/{tarea_id}", response_model=Tarea, tags=["Tareas"])
def actualizar_tarea(tarea_id: int, tarea_in: TareaUpdate):
    for index, tarea in enumerate(db_tareas):
        if tarea.id == tarea_id:
            # Actualizamos solo los campos que nos mandaron
            datos_actualizados = tarea.dict(exclude_unset=True)
            tarea_data = tarea.copy(update=datos_actualizados)
            db_tareas[index] = tarea_data
            return tarea_data
            
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

# DELETE: Borrar una tarea
@app.delete("/tareas/{tarea_id}", tags=["Tareas"])
def eliminar_tarea(tarea_id: int):
    for index, tarea in enumerate(db_tareas):
        if tarea.id == index + 1 or tarea.id == tarea_id: # Ajuste simple de índice
            db_tareas.pop(index)
            return {"mensaje": f"Tarea {tarea_id} eliminada con éxito"}
            
    raise HTTPException(status_code=404, detail="Tarea no encontrada")