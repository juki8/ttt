from helpers import Person, check

# Settings
bd_dict = {}

# Import persons
jk = Person('Julius', '11.04.1983')
pk = Person('Paula', '11.01.1986')
ak = Person('Toni', '16.12.2013')
lk = Person('Louise', '05.05.2017')

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
