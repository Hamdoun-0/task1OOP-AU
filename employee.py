from random import randint

class Employee:
    def __init__(self,name,family,manager=None):
        self.name=name
        self.id=randint(1000,9999)
        self.family=family.copy()
        self.manager=manager
        self.salary=2500

    @property
    def get_id(self):
        return self.id
    
    @property
    def get_family(self):
        return self.family



        
