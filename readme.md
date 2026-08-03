# 🚀 API REST de Tareas con FastAPI y SQLAlchemy

API backend moderna y liviana desarrollada con **FastAPI** y **SQLAlchemy**, diseñada para gestionar tareas con persistencia en una base de datos relacional (SQLite).

## 🛠️ Tecnologías utilizadas
* **Python 3.10+**
* **FastAPI** (Framework web asíncrono)
* **SQLAlchemy** (ORM para la gestión de base de datos)
* **Pydantic v2** (Validación de datos)
* **Uvicorn** (Servidor ASGI)
* **SQLite** (Base de datos local)

## 📁 Estructura del Proyecto
```text
backend-proyectos/
│
├── main.py          # Endpoints de la API (Rutas CRUD)
├── models.py        # Modelos Pydantic y SQLAlchemy de las tareas
├── database.py      # Configuración de la conexión a la base de datos
├── requirements.txt # Dependencias del proyecto
└── README.md        # Documentación del proyecto