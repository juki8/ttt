from helpers import san, check_win, board

## DEALING WITH INPUT // GAME SERVER

# Starting board
game = [[0, 0, 0],
	[0, 0, 0],
	[0, 0, 0]]

guesses = 0

while True:
   
## Ask player A for input
    a = input("Player A: Which case? - use: row,col: ")
    if a == "exit":
        break
    # Make sure that input is correct
    while san(a) == False:
        a = input("Wrong input! \nTry again, Player A: Which case? - use: row,col: ")
        if a == "exit":
            break
    if san(a) == True:
    # check if field is taken
        while game[int(a[0])-1][int(a[2])-1] != 0:
            a = input("Field taken! \nTry again, Player A: Which case? - use: row,col: ")
    # Fill field and add to guesses
        if game[int(a[0])-1][int(a[2])-1] == 0:
            game[int(a[0])-1][int(a[2])-1] = 1
            guesses += 1

    # Checks wins
            if check_win(game) == 1:
                print("Player A has won!!")
                board(game)
                break
                
            elif check_win(game) == 2:
                print("Player B has won!!")
                board(game)
                break
    
        board(game)
    
    # Check if fields are available
        if guesses == 9:
            print("all fields taken")
            break
    
## Ask player B for input
    a = input("Player B: Which case? - use: row,col: ")
    if a == "exit":
        break
    
    # Make sure that input is correct
    while san(a) == False:
        a = input("Wrong input! \nTry again, Player B: Which case? - use: row,col: ")
        if a == "exit":
            break
        
    if san(a) == True:
        while game[int(a[0])-1][int(a[2])-1] != 0:
            a = input("Field taken! \nTry again, Player B: Which case? - use: row,col: ")
        if game[int(a[0])-1][int(a[2])-1] == 0:
            game[int(a[0])-1][int(a[2])-1] = 2
            guesses += 1
    
    # Checks wins
            if check_win(game) == 1:
                print("Player A has won!!")
                board(game)
                break
            elif check_win(game) == 2:
                print("Player B has won!!")
                board(game)
                break
        board(game)
        
    # Check if fields are available
        if guesses == 9:
            print("all fields taken")
            break