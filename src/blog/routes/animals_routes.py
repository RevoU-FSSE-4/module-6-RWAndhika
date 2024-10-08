from flask import Blueprint, request
from blog.repositories.animals_repository import AnimalsRepository
from blog.services.animals_service import AnimalsService
from flasgger import swag_from

animals_blueprint = Blueprint("animals", __name__)

repository: AnimalsRepository = AnimalsRepository()
service: AnimalsService = AnimalsService(repository=repository)

@animals_blueprint.route("/animals", methods=["POST"])
@swag_from("../docs/register_animal.yml")
def register_animal():
    animal = request.get_json()
    try:
        animal = service.register_animal(animal)
    except ValueError as e:
        return {"error": str(e)}, 400
    
    return animal, 201

@animals_blueprint.route("/animals/<string:id>", methods=["GET"])
@swag_from("../docs/get_animal.yml")
def get_animal(id):
    animal = service.get_animal(id)
    if animal is None:
        return {"error": "Animal not found"}, 404
    
    return animal

@animals_blueprint.route("/animals/<string:id>", methods=["DELETE"])
@swag_from("../docs/delete_animal.yml")
def delete_animal(id):
    animal = service.delete_animal(id)
    if animal is None:
        return {"error": "Animal not found"}, 404
    
    return {"message": "Animal deleted succesfully"}, 200

@animals_blueprint.route("/animals", methods=["GET"])
@swag_from("../docs/list_animal.yml")
def get_all():
    animal = service.get_all()
    if len(animal) == 0:
        return {"error": "Animal list is empty"}, 404
    
    return animal

@animals_blueprint.route("/animals/<string:id>", methods=["PUT"])
@swag_from("../docs/update_animal.yml")
def update_animal(id):
    new_animal = request.get_json()
    animal = service.get_animal(id)
    if animal is None:
        return {"error": "Animal not found"}, 404
    
    try:
        new_animal = service.update_animal(new_animal, id)
    except ValueError as e:
        return {"error": str(e)}, 400
    
    return new_animal, 201