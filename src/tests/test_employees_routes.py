from flask import json
from unittest.mock import MagicMock
from blog.routes import employees_routes


def test_register_employee(client):
    employees_routes.service = MagicMock()
    employee = {
        "id": 1,
        "name": "Name 1",
        "email": "Email 1",
        "phonenumber": "1234567890",
        "role": "Role 1",
        "schedule": "Friday"
    }
    employees_routes.service.register_employee.return_value = employee

    response = client.post(
        "/employees", data=json.dumps(employee), content_type="application/json"
    )

    employees_routes.service.register_employee.assert_called_once_with(employee)
    assert response.status_code == 201
    assert json.loads(response.get_data()) == employee
    
def test_get_employee(client):
    employees_routes.service = MagicMock()
    employee = {
        "id": 1,
        "name": "Name 1",
        "email": "Email 1",
        "phonenumber": "1234567890",
        "role": "Role 1",
        "schedule": "Friday"
    }
    employees_routes.service.get_employee.return_value = employee

    response = client.get("/employees/1")

    employees_routes.service.get_employee.assert_called_once_with("1")
    assert response.status_code == 200
    assert json.loads(response.get_data()) == employee

def test_get_employee_not_found(client):
    employees_routes.service = MagicMock()
    employees_routes.service.get_employee.return_value = None

    response = client.get("/employees/1")

    employees_routes.service.get_employee.assert_called_once_with("1")
    assert response.status_code == 404
    assert json.loads(response.get_data()) == {"error": "Employee not found"}

def test_delete_employee(client):
    employees_routes.service = MagicMock()
    employee = {
        "id": 1,
        "name": "Name 1",
        "email": "Email 1",
        "phonenumber": "1234567890",
        "role": "Role 1",
        "schedule": "Friday"
    }
    employees_routes.service.delete_employee.return_value = employee

    response = client.delete("/employees/1")

    employees_routes.service.delete_employee.assert_called_once_with("1")
    assert response.status_code == 200

def test_delete_employee_not_found(client):
    employees_routes.service = MagicMock()
    employees_routes.service.delete_employee.return_value = None

    response = client.delete("/employees/1")

    employees_routes.service.delete_employee.assert_called_once_with("1")
    assert response.status_code == 404
    assert json.loads(response.get_data()) == {"error": "Employee not found"}

def test_update_employee(client):
    employees_routes.service = MagicMock()
    employee = {
        "id": 1,
        "name": "Name 1",
        "email": "Email 1",
        "phonenumber": "1234567890",
        "role": "Updated Role 2",
        "schedule": "Friday"
    }
    employees_routes.service.update_employee.return_value = employee

    response = client.put(
        "/employees/1", data=json.dumps(employee), content_type="application/json"
    )

    employees_routes.service.update_employee.assert_called_once_with(employee, "1")
    assert response.status_code == 201
    assert json.loads(response.get_data()) == employee