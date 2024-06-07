from flask import request, Blueprint, jsonify
from repository import employees
from flasgger import swag_from

employees_blueprint = Blueprint("employees", __name__)

@employees_blueprint.route("/employees", methods=["POST"])
@swag_from("docs/register_employee.yml")
def register_employee():
    name = request.json.get("name")
    email = request.json.get("email")
    phonenumber = request.json.get("phonenumber")
    role = request.json.get("role")
    schedule = request.json.get("schedule")

    if not name or not email or not phonenumber or not role or not schedule:
        return jsonify({"message": "All field are required"}), 400
    
    new_employee = {
        "id": employees[-1]["id"] + 1 if employees else 1,
        "name": name,
        "email": email,
        "phonenumber": phonenumber,
        "role": role,
        "schedule": schedule
    }

    employees.append(new_employee)
    return jsonify({"message": "employee created"}), 201

@employees_blueprint.route("/employees", methods=["GET"])
@swag_from("docs/list_employee.yml")
def get_employees():
    if len(employees) == 0:
        return jsonify({"error": "employee list is empty!"}), 404
    return jsonify(employees), 200

@employees_blueprint.route("/employees/<int:employee_id>", methods=["GET"])
@swag_from("docs/get_employee.yml")
def get_employee(employee_id):
    for employee in employees:
        if employee.get("id") == employee_id:
            return jsonify(employee), 200
        
    return jsonify({"error": "employee not found!"}), 404

@employees_blueprint.route("/employees/<int:employee_id>", methods=["PUT"])
@swag_from("docs/update_employee.yml")
def update_employee(employee_id):
    for employee in employees:
        if employee.get("id") == employee_id:
            employee["name"] = request.json.get("name", employee["name"])
            employee["email"] = request.json.get("email", employee["email"])
            employee["phonenumber"] = request.json.get("phonenumber", employee["phonenumber"])
            employee["role"] = request.json.get("role", employee["role"])
            employee["schedule"] = request.json.get("schedule", employee["schedule"])
            return jsonify(employee), 200
    
    return jsonify({"error": "employee not found!"}), 404

@employees_blueprint.route("/employees/<int:employee_id>", methods=["DELETE"])
@swag_from("docs/delete_employee.yml")
def delete_employee(employee_id):
    for employee in employees:
        if employee.get("id") == employee_id:
            employees.remove(employee)
            return jsonify({"message": "employee deleted succesfully"}), 200
        
    return jsonify({"error": "employee not found!"}), 404