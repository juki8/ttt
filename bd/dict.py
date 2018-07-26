from helpers import Person, check_dict, im_persons, create_dict, check

# Import persons
im_persons()

# Creact dict via helpers function
bd_dict = create_dict()
#print(bd_dict)

# Give names of everyone in dict
print("Welcome to the birthday dictionary. We know the birthdays of: ")
for person in Person.instances:
    print(Person.get_name(person))

# Get user input
while True:
    a = input("Who's birthday do you want to look up? ")
    if a == "exit":
        break
    check(a)
    check_dict(a, bd_dict)