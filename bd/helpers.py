class Person (object):
    instances = []
    def __init__(self, name, bd):
        self.name = name
        self.bd = bd
        Person.instances.append(self)

    def get_name(self):
        return self.name

    def get_bd (self):
        return self.bd
    
    def add_dict(self, b_dict):
        b_dict[self.name] = self.bd
    
    def __str__(self):
        return str(self.name) + "'s birthday is " + str(self.bd) + "."

def check(a):
'''
Checks if input a is name of a Person
'''
    result = 0
    for person in Person.instances:
        if Person.get_name(person) == a:
            result += 1
    if result == 0:
        print("Not in list")
    elif result == 1:
        print(Person.get_bd(person))
