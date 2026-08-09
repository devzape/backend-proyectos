# ✅ API REST de Gestión de Tareas con FastAPI y SQLAlchemy

API desarrollada con **FastAPI** para la gestión de tareas, con **SQLite** como base de datos, **SQLAlchemy** como ORM y una suite de pruebas automatizadas con **Pytest**.

<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi" />
  <img src="https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white" />
  <img src="https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white" />
</p>

## 🛠️ Tecnologías

- **FastAPI** — framework web para construir la API
- **SQLAlchemy** — ORM para la gestión de la base de datos
- **Pydantic V2** — validación de datos y esquemas tipados
- **Pytest** — tests unitarios y de integración
- **SQLite** — base en disco para producción, en memoria para tests

## ⚙️ Cómo correr el proyecto localmente

```bash
# 1. Clonar el repositorio
git clone https://github.com/devzape/backend-proyectos.git
cd backend-proyectos

# 2. Crear y activar un entorno virtual
python -m venv venv
source venv/bin/activate   # En Windows: venv\Scripts\activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Levantar el servidor
uvicorn main:app --reload
```

La API queda disponible en `http://127.0.0.1:8000` y la documentación interactiva en `http://127.0.0.1:8000/docs`.

## 🧪 Correr los tests

```bash
pytest
```

## 📁 Estructura del proyecto

```
backend-proyectos/
├── main.py            # Endpoints de la API y esquemas Pydantic
├── database.py        # Configuración de la conexión a la BD
├── models.py          # Modelos de SQLAlchemy
├── test_main.py        # Suite de pruebas automatizadas
└── requirements.txt   # Dependencias del proyecto
```

## 🚧 Próximas mejoras

- [ ] Agregar autenticación de usuarios
- [ ] Mover la config de la BD a variables de entorno
- [ ] Sumar CI con GitHub Actions para correr los tests en cada push

---

> 💡 Nota: la base de datos (`database.db`) no debería versionarse — se recomienda agregarla al `.gitignore`.
