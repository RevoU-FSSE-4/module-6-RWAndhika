class EmployeesRepository:
    def __init__(self):
        self.employees = {}
        self.id = 1

    def get_all(self):
        return list(self.employees.values())

    def register_employee(self, employee):
        employee["id"] = self.id
        self.employees[self.id] = employee
        self.id += 1
        return employee
    
    def get_employee(self, id):
        return self.employees.get(id)
    
    def delete_employee(self, id):
        return self.employees.pop(id, None)
    
    def update_employee(self, employee, id):
        employee["id"] = id
        self.employees[id] = employee
        return employee