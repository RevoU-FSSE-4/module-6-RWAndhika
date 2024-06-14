from blog.repositories.animals_repository import AnimalsRepository

class AnimalsService:
    def __init__(self, repository):
        self.repository: AnimalsRepository = repository

    def validate_animal(self, animal):
        species = animal.get("species")
        age = animal.get("age")
        gender = animal.get("gender")
        special_requirements = animal.get("special_requirements")

        if not species or not isinstance(species, str):
            raise ValueError("Animal's species must be a string")
        
        if age < 0 or not isinstance(age, int):
            raise ValueError("Animal's age must be an integer and a whole number ")
        
        if not gender or not isinstance(gender, str):
            raise ValueError("Animal's gender must be a string")
        
        if not special_requirements or not isinstance(special_requirements, str):
            raise ValueError("Animal's special requirements must be a string")
                
    def register_animal(self, animal):
        self.validate_animal(animal)
        return self.repository.register_animal(animal)
    
    def get_animal(self, id):
        return self.repository.get_animal(int(id))
    
    def delete_animal(self, id):
        return self.repository.delete_animal(int(id))
    
    def get_all(self):
        return self.repository.get_all()
    
    def update_animal(self, animal, id):
        self.validate_animal(animal)
        return self.repository.update_animal(animal, int(id))