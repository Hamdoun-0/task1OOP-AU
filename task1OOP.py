from employee import Employee





if __name__ == '__main__' :
    
    name='John Smith'
    boss = Employee('Jane Redmond', {})
    family={
        'son':  {
            'insured':True,
            'Age':16
                },

        'Wife': {
            'insured':False,
            'Age':32
                }
            }
    

    my_employee = Employee (name, family, boss)
    not_boss = Employee ('Adam Cater', {})
    # do not change:
    print(id(my_employee.family))
    print(id(my_employee.get_family)) 
    boss.apply_raise(my_employee, 25)
    print(not_boss.apply_raise(my_employee, 25))