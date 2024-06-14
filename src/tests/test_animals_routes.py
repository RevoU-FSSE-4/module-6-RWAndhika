from flask import json
from unittest.mock import MagicMock
from blog.routes import animals_routes

def test_register_animal(client):
    animals_routes.service = MagicMock()
    animal = {
        "id": 1,
        "species": "Species 1",
        "age": 3,
        "gender": "Male",
        "special_requirements": "None"
    }
    animals_routes.service.register_animal.return_value = animal

    response = client.post("/animals", data=json.dumps(animal), content_type="application/json")

    animals_routes.service.register_animal.assert_called_once_with(animal)
    assert response.status_code == 201
    assert json.loads(response.get_data()) == animal

def test_get_animal(client):
    animals_routes.service = MagicMock()
    animal = {
        "id": 1,
        "species": "Species 1",
        "age": 3,
        "gender": "Male",
        "special_requirements": "None"
    }
    animals_routes.service.get_animal.return_value = animal

    response = client.get("/animals/1")

    animals_routes.service.get_animal.assert_called_once_with("1")
    assert response.status_code == 200
    assert json.loads(response.get_data()) == animal

def test_get_animal_not_found(client):
    animals_routes.service = MagicMock()
    animals_routes.service.get_animal.return_value = None

    response = client.get("/animals/1")

    animals_routes.service.get_animal.assert_called_once_with("1")
    assert response.status_code == 404
    assert json.loads(response.get_data()) == {"error": "Animal not found"}

def test_delete_animal(client):
    animals_routes.service = MagicMock()
    animal = {
        "id": 1,
        "species": "Species 1",
        "age": 3,
        "gender": "Male",
        "special_requirements": "None"
    }
    animals_routes.service.delete_animal.return_value = animal

    response = client.delete("/animals/1")

    animals_routes.service.delete_animal.assert_called_once_with("1")
    assert response.status_code == 200

def test_delete_animal_not_found(client):
    animals_routes.service = MagicMock()
    animals_routes.service.delete_animal.return_value = None

    response = client.delete("/animals/1")

    animals_routes.service.delete_animal.assert_called_once_with("1")
    assert response.status_code == 404
    assert json.loads(response.get_data()) == {"error": "Animal not found"}

def test_update_animal(client):
    animals_routes.service = MagicMock()
    animal = {
        "id": 1,
        "species": "Edited Species 2",
        "age": 3,
        "gender": "Male",
        "special_requirements": "None"
    }
    animals_routes.service.update_animal.return_value = animal

    response = client.put("/animals/1", data=json.dumps(animal), content_type="application/json")

    animals_routes.service.update_animal.assert_called_once_with(animal, "1")
    assert response.status_code == 201
    assert json.loads(response.get_data()) == animal