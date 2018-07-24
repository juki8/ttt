## HELPER FUNCTIONS: 

# Function to sanitize overall input
def san(a):   
    '''Takes the user input and checks if valid 
    (3 chars, 2 ints between 1 and 3 
    Returns True if valid, False if not valid'''

    if len(a) != 3:
#        print("Wrong input.")
        return False
    else:
        return san_part(a[0]) and san_part(a[2])

# Function to sanitize parts of the input
def san_part(a0):
    '''Checks if parts of the input are valid.
    Returns True if valid, False if not valid'''
    while True:
       try:
           a0 = int(a0) # checks if input is int
       except ValueError: 
#           print("Not a number!")
           return False
       else:
           if a0 in range (1, 4): # checks if input in range
               return True
               break
           else:
#               print ('Try again.')
               return False


## DEALING WITH INPUT // GAME SERVER
# Starting board
game = [[0, 0, 0],
	[0, 0, 0],
	[0, 0, 0]]

guesses = 0

while True:
    # Ask player A for input
    a = input("Player A: Which case? - use: row,col: ")
    if a == "exit":
        break
    
    while san(a) == False:
        a = input("Wrong input! Try again, Player A: Which case? - use: row,col: ")
        if a == "exit":
            break
    if san(a) == True:
        # check field is taken
        while game[int(a[0])-1][int(a[2])-1] != 0:
            a = input("Field taken! Try again, Player A: Which case? - use: row,col: ")
        # Fill field and add to guesses
        if game[int(a[0])-1][int(a[2])-1] == 0:
            game[int(a[0])-1][int(a[2])-1] = 1
            guesses += 1
    
        print(game)
    
        # Check if fields are available
        if guesses == 9:
            print("all fields taken")
            break
    
    # Ask player B for input
    a = input("Player B: Which case? - use: row,col: ")
    if a == "exit":
        break
    
    while san(a) == False:
        a = input("Wrong input! Try again, Player B: Which case? - use: row,col: ")
        if a == "exit":
            break
        
    if san(a) == True:
        while game[int(a[0])-1][int(a[2])-1] != 0:
            a = input("Field taken! Try again, Player B: Which case? - use: row,col: ")
        if game[int(a[0])-1][int(a[2])-1] == 0:
            game[int(a[0])-1][int(a[2])-1] = 2
            guesses += 1
        print(game)
        
        # Check if fields are available
        if guesses == 9:
            print("all fields taken")
            break

  
    



