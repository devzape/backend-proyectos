from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
import pytest

import database
import models
from main import app, get_db

SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

database.Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

# FIXTURE: Limpia la base de datos antes de cada test para que sean independientes
@pytest.fixture(autouse=True)
def limpiar_bd():
    db = TestingSessionLocal()
    db.query(models.TareaDB).delete()
    db.commit()
    db.close()


def test_obtener_tareas_vacia():
    response = client.get("/tareas")
    assert response.status_code == 200
    assert response.json() == []


def test_crear_tarea():
    response = client.post(
        "/tareas",
        json={
            "titulo": "Testear la API con pytest",
            "descripcion": "Automatizando pruebas de nivel senior",
            "completada": False
        }
    )
    assert response.status_code == 201
    data = response.json()
    assert data["titulo"] == "Testear la API con pytest"
    assert "id" in data


def test_obtener_tarea_no_existente():
    response = client.get("/tareas/99999")
    assert response.status_code == 404
    assert response.json()["detail"] == "La tarea con el ID 99999 no existe."


def test_actualizar_tarea():
    response_crear = client.post(
        "/tareas",
        json={"titulo": "Tarea vieja", "descripcion": "Actualizar esto", "completada": False}
    )
    tarea_id = response_crear.json()["id"]

    response = client.put(
        f"/tareas/{tarea_id}",
        json={"titulo": "Tarea actualizada", "descripcion": "Ya fue modificada", "completada": True}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["titulo"] == "Tarea actualizada"
    assert data["completada"] is True


def test_eliminar_tarea():
    response_crear = client.post(
        "/tareas",
        json={"titulo": "Para borrar", "descripcion": "Chau", "completada": False}
    )
    tarea_id = response_crear.json()["id"]

    response = client.delete(f"/tareas/{tarea_id}")
    assert response.status_code == 204

    response_get = client.get(f"/tareas/{tarea_id}")
    assert response_get.status_code == 404


def test_filtrar_tareas():
    client.post("/tareas", json={"titulo": "Pendiente 1", "completada": False})
    client.post("/tareas", json={"titulo": "Completada 1", "completada": True})

    response_completadas = client.get("/tareas?completada=true")
    assert response_completadas.status_code == 200
    data_completadas = response_completadas.json()
    assert len(data_completadas) == 1
    assert data_completadas[0]["titulo"] == "Completada 1"

    response_pendientes = client.get("/tareas?completada=false")
    assert response_pendientes.status_code == 200
    data_pendientes = response_pendientes.json()
    assert len(data_pendientes) == 1
    assert data_pendientes[0]["titulo"] == "Pendiente 1"