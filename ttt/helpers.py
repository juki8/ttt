## CHECK WINS (ex26)

def check_win(L):
    ''' Takes L, a list of 3 lists with three items each. 
        Items are 0, 1, or 2.
        Checks if player 1 or 2 has won'''
    
    # horizontal wins
    for I in L:
        if (I[0] == I[1]) and (I[0] == I[2]) == True:
            if I[0] == 1:
                print("1 has won")
                break
            elif I[0] == 2:
                print("2 has won")
                break
 
    # vertical wins
    if (L[0][0] == L[1][0]) and (L[0][0] == L[2][0]) == True:
        if L[0][0] == 1:
            print("1 has won")
        elif L[0][0] == 2:
            print("2 has won")
    
    elif (L[0][1] == L[1][1]) and (L[0][1] == L[2][1]) == True:
        if L[0][1] == 1:
            print("1 has won")
        elif L[0][1] == 2:
            print("2 has won")

    elif (L[0][2] == L[1][2]) and (L[0][2] == L[2][2]) == True:
        if L[0][2] == 1:
            print("1 has won")
        elif L[0][2] == 2:
            print("2 has won")
    
    # diagonal wins indexed 
    elif (L[0][0] == L[1][1]) and (L[0][0] == L[2][2]) == True:
        if L[0][0] == 1:
            print("1 has won")
        elif L[0][0] == 2:
            print("2 has won")  

    elif (L[0][2] == L[1][1]) and (L[0][2] == L[2][0]) == True:
        if L[0][2] == 1:
            print("1 has won")
        elif L[0][2] == 2:
            print("2 has won")

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

## FUNCTIONS TO SANITIZE INPUT
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
           else:
#               print ('Try again.')
               return False
