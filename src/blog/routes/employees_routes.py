from flask import Blueprint, request
from blog.repositories.employees_repository import EmployeesRepository
from blog.services.employees_service import EmployeesService
# from flasgger import swag_from

employees_blueprint = Blueprint("employees", __name__)

repository: EmployeesRepository = EmployeesRepository()
service: EmployeesService = EmployeesService(repository=repository)

@employees_blueprint.route("/employees", methods=["POST"])
def register_employee():
    employee = request.get_json()
    try:
        employee = service.register_employee(employee)
    except ValueError as e:
        return {"error": str(e)}, 400
    
    return employee, 201

@employees_blueprint.route("/employees/<string:id>", methods=["GET"])
def get_employee(id):
    employee = service.get_employee(id)
    if employee is None:
        return {"error": "Employee not found"}, 404
    
    return employee

@employees_blueprint.route("/employees/<string:id>", methods=["DELETE"])
def delete_employee(id):
    employee = service.delete_employee(id)
    if employee is None:
        return {"error": "Employee not found"}, 404
    
    return {"message": "Employee deleted succesfully"}, 200

@employees_blueprint.route("/employees", methods=["GET"])
def get_all():
    employee = service.get_all()
    return employee

@employees_blueprint.route("/employees/<string:id>", methods=["PUT"])
def update_employee(id):
    new_employee = request.get_json()
    employee = service.get_employee(id)
    if employee is None:
        return {"error": "Employee not found"}, 404
    
    try:
        new_employee = service.update_employee(new_employee, id)
    except ValueError as e:
        return {"error": str(e)}, 400
    
    return new_employee, 201