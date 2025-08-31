from random import randint

class Employee:
    def __init__(self,name,family,manager=None):
        self.name=name
        self.id=randint(1000,9999)
        self.family=family
        self.manager=manager
        self.salary=2500

    @property
    def get_id(self):
        return self.id
    
    @property
    def get_family(self):
        return self.family.copy()
    
    
    def apply_raise(self, managed_employee: 'Employee', raise_percent: int):
        if managed_employee.manager is self:
           managed_employee.salary += (managed_employee.salary * (raise_percent/100))
           print(managed_employee.salary)
           return True
        elif ():
            return 
            
        # you must handle error where managed_employee._manager isn't self
        # choose to return success status or raise exceptions


