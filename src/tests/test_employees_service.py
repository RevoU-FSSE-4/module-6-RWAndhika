from unittest.mock import MagicMock
import pytest
from blog.services.employees_service import EmployeesService


@pytest.fixture
def service():
    repository = MagicMock()
    return EmployeesService(repository)

@pytest.mark.parametrize(
    "employee, expected_exception",
    [
        (
            {
                "id": 1,
                "name": 3,
                "email": "Email 1",
                "phonenumber": "1234567890",
                "role": "Role 1",
                "schedule": "Friday"
            },
            ValueError
        ),
        (
            {
                "id": 1,
                "name": "Name 1",
                "email": 321,
                "phonenumber": "1234567890",
                "role": "Role 1",
                "schedule": "Friday"
            },
            ValueError
        ),
        (
            {
                "id": 1,
                "name": "Name 1",
                "email": "Email 1",
                "phonenumber": "",
                "role": "Role 1",
                "schedule": "Friday"
            },
            ValueError
        ),
        (
            {
                "id": 1,
                "name": "Name 1",
                "email": "Email 1",
                "phonenumber": "231903219",
                "role": "",
                "schedule": "Friday"
            },
            ValueError
        ),
        (
            {
                "id": 1,
                "name": "Name 1",
                "email": "Email 1",
                "phonenumber": "231903219",
                "role": "Role 1",
                "schedule": ""
            },
            ValueError
        )
    ]
)
def test_validate_employee(service, employee, expected_exception):
    with pytest.raises(expected_exception):
        service.validate_employee(employee)

def test_register_employee(service):
    employee = {
        "id": 1,
        "name": "Name 1",
        "email": "Email 1",
        "phonenumber": "123456789",
        "role": "Role 1",
        "schedule": "Friday"
    }
    service.repository.register_employee.return_value = employee

    result = service.register_employee(employee)

    service.repository.register_employee.assert_called_once_with(employee)
    assert result == employee

def test_get_employee(service):
    employee = {
        "id": 1,
        "name": "Name 1",
        "email": "Email 1",
        "phonenumber": "123456789",
        "role": "Role 1",
        "schedule": "Friday"
    }
    service.repository.get_employee.return_value = employee

    result = service.get_employee(1)

    service.repository.get_employee.assert_called_once_with(1)
    assert result == employee

def test_delete_employee(service):
    employee = {
        "id": 1,
        "name": "Name 1",
        "email": "Email 1",
        "phonenumber": "123456789",
        "role": "Role 1",
        "schedule": "Friday"
    }
    service.repository.delete_employee.return_value = employee

    result = service.delete_employee(1)

    service.repository.delete_employee.assert_called_once_with(1)
    assert result == employee

def test_update_employee(service):
    employee = {
        "id": 1,
        "name": "Name 1",
        "email": "Email 1",
        "phonenumber": "123456789",
        "role": "Role 1",
        "schedule": "Friday"
    }
    service.repository.update_employee.return_value = employee

    result = service.update_employee(employee, 1)

    service.repository.update_employee.assert_called_once_with(employee, 1)
    assert result == employee