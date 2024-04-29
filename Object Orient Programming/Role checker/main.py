class Employee():
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def __str__(self):
        return f"Employee: {self.name}, ID: {self.id}"
    
    def __eq__(self, other):
        if isinstance(other, Employee):
            return self.id == other.id
        else:
            return False
        
    def __add__(self, other):
        raise ValueError("Can not add employees!")
    
class Manager(Employee):
    def __init__(self, name, id, deparment):
        super().__init__(name, id)
        self.department = deparment
        
    def __str__(self):
        return f"Manager: {self.name}, ID: {self.id}, Department: {self.department}"
    
    def __eq__(self, other):
        if isinstance(other, Employee):
            return self.id == other.id
        else:
            return False
        
    def __add__(self, other):
        raise ValueError("Can not add managers!")
    
class Staff(Employee):
    def __init__(self, name, id, role):
        super().__init__(name, id)
        self.role = role
        
    def __str__(self):
        return f"Staff: {self.name}, ID: {self.id}, Role: {self.role}"
    
    def __eq__(self, other):
        if isinstance(other, Employee):
            return self.id == other.id
        else:
            return False
        
    def __add__(self, other):
        raise ValueError("Can not add staff members!")
    

employee1 = Employee("Jones", 1)
employee2 = Employee("Jefke", 2)

manager1 = Manager("Storm", 10, "Marketing")
manager2 = Manager("Sky", 11, "Sales")

staff1 = Staff("Sam", 15, "DevOps")
staff2 = Staff("Alice", 16, "Support Engineer")


print(employee1)
print(employee2)
print(manager1)
print(manager2)
print(staff1)
print(staff2)

print(employee1 == employee2)
print(staff1 == staff2)

print(manager1 + manager2)