from blog.repositories.employees_repository import EmployeesRepository

class EmployeesService:
    def __init__(self, repository):
        self.repository: EmployeesRepository = repository

    def validate_employee(self, employee):
        name = employee.get("name")
        email = employee.get("email")
        phonenumber = employee.get("phonenumber")
        role = employee.get("role")
        schedule = employee.get("schedule")

        if not name or not isinstance(name, str):
            raise ValueError("Employee's name must be a string")
        
        if not email or not isinstance(email, str):
            raise ValueError("Employee's email must be a string")
        
        if not phonenumber or not isinstance(phonenumber, str):
            raise ValueError("Employee's phonenumber must be a string")
        
        if not role or not isinstance(role, str):
            raise ValueError("Employee's role must be a string")
        
        if not schedule or not isinstance(schedule, str):
            raise ValueError("Employee's schedule must be a string")
        
    def register_employee(self, employee):
        self.validate_employee(employee)
        return self.repository.register_employee(employee)
    
    def get_employee(self, id):
        return self.repository.get_employee(int(id))
    
    def delete_employee(self, id):
        return self.repository.delete_employee(int(id))
    
    def get_all(self):
        return self.repository.get_all()
    
    def update_employee(self, employee, id):
        self.validate_employee(employee)
        return self.repository.update_employee(employee, int(id))