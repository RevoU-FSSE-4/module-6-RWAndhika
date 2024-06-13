class AnimalsRepository:
    def __init__(self):
        self.animals = {}
        self.id = 1

    def get_all(self):
        return list(self.animals.values())

    def register_animal(self, animal):
        animal["id"] = self.id
        self.animals[self.id] = animal
        self.id += 1
        return animal
    
    def get_animal(self, id):
        return self.animals.get(id)
    
    def delete_animal(self, id):
        return self.animals.pop(id, None)
    
    def update_animal(self, animal, id):
        animal["id"] = id
        self.animals[id] = animal
        return animal