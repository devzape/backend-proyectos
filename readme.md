# 🚀 API REST de Tareas con FastAPI y SQLAlchemy

API backend moderna y liviana desarrollada con **FastAPI** y **SQLAlchemy**, diseñada para gestionar tareas con persistencia en una base de datos relacional (SQLite), manejo robusto de excepciones y un CRUD completo.

## 🛠️ Tecnologías utilizadas
* **Python 3.10+**
* **FastAPI** (Framework web asíncrono)
* **SQLAlchemy** (ORM para la gestión de base de datos)
* **Pydantic v2** (Validación de datos y esquemas de actualización)
* **Uvicorn** (Servidor ASGI)
* **SQLite** (Base de datos local)

## 📌 Endpoints de la API (CRUD Completo)
* `GET /tareas` - Lista todas las tareas registradas.
* `POST /tareas` - Crea una nueva tarea (Código `201 Created`).
* `GET /tareas/{id}` - Obtiene el detalle de una tarea específica (Con manejo de error `404 Not Found`).
* `PUT /tareas/{id}` - Actualiza parcial o totalmente una tarea existente.
* `DELETE /tareas/{id}` - Elimina una tarea por su ID (Código `204 No Content`).

## 📁 Estructura del Proyecto
```text
backend-proyectos/
│
├── main.py          # Endpoints de la API, lógica de rutas y excepciones HTTP
├── models.py        # Esquemas Pydantic y Modelos ORM de SQLAlchemy
├── database.py      # Configuración de la conexión a la base de datos
├── requirements.txt # Dependencias del proyecto
└── README.md        # Documentación del proyecto