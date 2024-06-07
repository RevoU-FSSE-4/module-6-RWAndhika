from flask import request, Blueprint, jsonify
from repository import animals
from flasgger import swag_from

animals_blueprint = Blueprint("animals", __name__)

@animals_blueprint.route("/animals", methods=["POST"])
def register_animals():
    species = request.json.get("species")
    age = request.json.get("age")
    gender = request.json.get("gender")
    special_requirements = request.json.get("special_requirements")

    if not species or not age or not gender or not special_requirements:
        return jsonify({"message": "All field are required"}), 400
    
    new_animal = {
        "id": animals[-1]["id"] + 1 if animals else 1,
        "species": species,
        "age": age,
        "gender": gender,
        "special_requirements": special_requirements
    }

    animals.append(new_animal)
    return jsonify({"message": "animal created"}), 201

@animals_blueprint.route("/animals", methods=["GET"])
def get_animals():
    return jsonify(animals), 200

@animals_blueprint.route("/animals/<int:animal_id>", methods=["GET"])
def get_animal(animal_id):
    for animal in animals:
        if animal.get("id") == animal_id:
            return jsonify(animal), 200
        
    return jsonify({"error": "animal not found!"}), 400

@animals_blueprint.route("/animals/<int:animal_id>", methods=["PUT"])
def update_animal(animal_id):
    for animal in animals:
        if animal.get("id") == animal_id:
            animal["species"] = request.json.get("species", animal["species"])
            animal["age"] = request.json.get("age", animal["age"])
            animal["gender"] = request.json.get("gender", animal["gender"])
            animal["special_requirements"] = request.json.get("special_requirements", animal["special_requirements"])
            return jsonify(animal), 200
    
    return jsonify({"error": "animal not found!"}), 400

@animals_blueprint.route("/animals/<int:animal_id>", methods=["DELETE"])
def delete_animal(animal_id):
    for animal in animals:
        if animal.get("id") == animal_id:
            animals.remove(animal)
            return jsonify({"result": True}), 200
        
    return jsonify({"error": "animal not found!"}), 400