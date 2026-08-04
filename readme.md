# 🚀 API REST de Gestión de Tareas con FastAPI y SQLAlchemy

API desarrollada en **FastAPI** para la gestión de tareas, utilizando **SQLite** como base de datos, **SQLAlchemy** como ORM y una suite completa de pruebas automatizadas con **Pytest**.

---

## 🛠️ Tecnologías Utilizadas

* **FastAPI**: Framework web moderno y de alto rendimiento para construir APIs.
* **SQLAlchemy**: ORM (Object-Relational Mapping) para la gestión de bases de datos relacionales.
* **Pydantic V2**: Validación de datos y esquemas tipados.
* **Pytest**: Framework para pruebas unitarias e integración.
* **SQLite**: Base de datos ligera (en disco para producción y en memoria para tests).

---

## 📂 Estructura del Proyecto

```text
backend-proyectos/
│
├── database.py       # Configuración de la conexión a la base de datos
├── models.py         # Modelos de SQLAlchemy (Tablas)
├── main.py           # Endpoints de la API y esquemas Pydantic
├── test_main.py      # Suite de pruebas automatizadas
├── requirements.txt  # Dependencias del proyecto
└── venv/             # Entorno virtual