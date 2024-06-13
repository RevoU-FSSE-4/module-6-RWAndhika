import pytest
from app import app
from flask import json
from unittest.mock import MagicMock

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_register_employee(client):
    employee_view = MagicMock()
    new_employee = {
        
        "name": "The name",
        "email": "email@yahoo.com",
        "phonenumber": "1234567890",
        "role": "role",
        "schedule": "Friday"
    }
    return_post = {
        "message": "employee created"
    }
    employee_view.register_employee.return_value = return_post

    response = client.post(
        "/employees", data=json.dumps(new_employee), content_type="application/json"
    )

    assert response.status_code == 201