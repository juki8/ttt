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
    Checks if input a is name of an existing Person
    '''
    result = 0
    for person in Person.instances:
        if Person.get_name(person) == a:
            result += 1
    if result == 0:
        print("Not in list")
    elif result == 1:
        print(Person.get_bd(person))


# Create dict
import json
def create_dict():
    '''
    Creates dict from Person instances.
    Returns dict labelled: "bd_dict"
    '''
    bd_dict = {}
    for person in Person.instances:
        Person.add_dict(person, bd_dict)
    # Create JSON
    # with open("dict.json", "w") as f:
    #     json.dump(bd_dict, f)

# Import persons
def im_persons():
    
    # import JSON
    with open("dict.json", "r") as f:
        datastore = json.loads(f.read())
    
    # select keys
    keys = []
    for i in datastore.keys():
        keys.append(i)
    print(keys)
    
    # iterate over keys and values to import 
    for i in range(len(datastore)):
        Person(keys[i], datastore[keys[i]])
