from unittest.mock import MagicMock
import pytest
from blog.services.animals_service import AnimalsService


@pytest.fixture
def service():
    repository = MagicMock()
    return AnimalsService(repository)

@pytest.mark.parametrize(
    "animal, expected_exception",
    [
        (
            {
                "id": 1,
                "species": "",
                "age": 3,
                "gender": "Male",
                "special_requirements": "None"
            },
            ValueError
        ),
        (
            {
                "id": 1,
                "species": "Species 1",
                "age": -10,
                "gender": "Male",
                "special_requirements": "None"
            },
            ValueError
        ),
        (
            {
                "id": 1,
                "species": "Species 1",
                "age": 3,
                "gender": 50,
                "special_requirements": "None"
            },
            ValueError
        ),
        (
            {
                "id": 1,
                "species": "Species 1",
                "age": 3,
                "gender": "Male",
                "special_requirements": ""
            },
            ValueError
        )
    ]
)
def test_validate_animal(service, animal, expected_exception):
    with pytest.raises(expected_exception):
        service.validate_animal(animal)

def test_register_animal(service):
    animal = {
        "id": 1,
        "species": "Species 1",
        "age": 3,
        "gender": "Male",
        "special_requirements": "None"
    }
    service.repository.register_animal.return_value = animal

    result = service.register_animal(animal)

    service.repository.register_animal.assert_called_once_with(animal)
    assert result == animal

def test_get_animal(service):
    animal = {
        "id": 1,
        "species": "Species 1",
        "age": 3,
        "gender": "Male",
        "special_requirements": "None"
    }
    service.repository.get_animal.return_value = animal

    result = service.get_animal(1)

    service.repository.get_animal.assert_called_once_with(1)
    assert result == animal

def test_delete_animal(service):
    animal = {
        "id": 1,
        "species": "Species 1",
        "age": 3,
        "gender": "Male",
        "special_requirements": "None"
    }
    service.repository.delete_animal.return_value = animal

    result = service.delete_animal(1)

    service.repository.delete_animal.assert_called_once_with(1)
    assert result == animal

def test_update_animal(service):
    animal = {
        "id": 1,
        "species": "Species 1",
        "age": 3,
        "gender": "Male",
        "special_requirements": "None"
    }
    service.repository.update_animal.return_value = animal

    result = service.update_animal(animal, 1)

    service.repository.update_animal.assert_called_once_with(animal, 1)
    assert result == animal