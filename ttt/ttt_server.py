from helpers import san 

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