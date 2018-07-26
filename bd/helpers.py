from collections import Counter
import json

class Person (object):
    '''
    Defines class with name and birthday
    '''
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
    Checks if input a is name of an existing Person.
    Uses the Person class
    Returns Birthday
    '''
    result = 0
    for person in Person.instances:
        if Person.get_name(person) == a:
            result += 1
            print(Person.get_bd(person))
    if result == 0:
        print("Not in list")

def check_dict(a, b_dict):
    '''
    Checks if input a is name of an existing Person.
    Uses the dict 
    Returns Birthday
    '''
    result = 0
    for person in b_dict:
        if person == a:
            result += 1
            print(b_dict[a])    
    if result == 0:
        print("Not in list")        

# Create dict
def create_dict():
    '''
    Creates dict from Person instances.
    Returns dict labelled: "bd_dict"
    '''
    bd_dict = {}
    for person in Person.instances:
        Person.add_dict(person, bd_dict)
    return bd_dict
    # Create JSON
    # with open("dict.json", "w") as f:
    #     json.dump(bd_dict, f)

# Import persons
def im_persons():
    
    # import JSON
    with open("dict.json", "r") as f:
        datastore = json.loads(f.read())    
    print(datastore)
    datastore = dict_months(datastore, 0)
    print(datastore)

    # select keys
    keys = []
    for i in datastore.keys():
        keys.append(i)
    # print(keys)
    
    # iterate over keys and values to import 
    for i in range(len(datastore)):
        Person(keys[i], datastore[keys[i]])

def dict_months(bd_dict, out):
    '''
    Transforms dates in months. Takes list and output form as two inputs: 
    input is date format: dd.mm.yyyy
    output is date format: dd. month yyyy
    output options: 0 = "fulldate" or 1 = "month only"
    return updated dictionary.  
    '''
    # Get dates
    list_dates = []
    for person in bd_dict:
        list_dates.append(bd_dict[person])
    
    # Extract months    
    list_months = []
    for i in range(len(list_dates)):
        list_months.append(list_dates[i][3:6])
    
    # Change months names
    list_monthnames = []
    for i in range(len(list_months)):
        if list_months[i] == "01.":
            list_monthnames.append("January")
        elif list_months[i] == "02.":
            list_monthnames.append("February")
        elif list_months[i] == "03.":
            list_monthnames.append("March")
        elif list_months[i] == "04.":
            list_monthnames.append("April")
        elif list_months[i] == "05.":
            list_monthnames.append("May")
        elif list_months[i] == "06.":
            list_monthnames.append("June")    
        elif list_months[i] == "07.":
            list_monthnames.append("July")
        elif list_months[i] == "08.":
            list_monthnames.append("August")
        elif list_months[i] == "09.":
            list_monthnames.append("September")
        elif list_months[i] == "10.":
            list_monthnames.append("October")
        elif list_months[i] == "11.":
            list_monthnames.append("November")
        elif list_months[i] == "12.":
            list_monthnames.append("December")

    # Complete date with monthnames
    list_newdates = []
    for i in range(len(list_monthnames)):
        list_newdates.append(list_dates[i][0:3] + " " + list_monthnames[i] + " " + list_dates[i][6:10])

    # Get keys
    keys = []
    for i in bd_dict.keys():
        keys.append(i)
     
    # Update dict 
    # for "fullmonth output"
    if out == 0:            
        for i in range(len(bd_dict)):
            bd_dict[keys[i]] = list_newdates[i] # To output full dates
    # for "month-only output"
    if out == 1:            
        for i in range(len(bd_dict)):
            bd_dict[keys[i]] = list_monthnames[i] # To output months only 

    return bd_dict

def month_count(b_dict):
    ''' Counts how many birthdays per month.
        Takes dict in format dd.mm.yyyy as input.
        Returns counter dict.
    '''
    D = dict_months(b_dict, 1)
    L = []
    for person in D:
        L.append(D[person])
    c = dict(Counter(L))
    return c

test = {'Julius': '11.04.1983', 'Paula': '11.04.1986', 'Toni': '16.12.2013', 'Louise': '05.05.2017', 'Lisa': '02.03.1979'}

