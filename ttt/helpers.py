## CHECK WINS (ex26)

def check_win(L):
    ''' Takes L, a list of 3 lists with three items each. 
        Items are 0, 1, or 2.
        Checks if player 1 or 2 has won'''
    
    # horizontal wins
    for I in L:
        if (I[0] == I[1]) and (I[0] == I[2]) == True:
            if I[0] == 1:
                return 1
                break
            elif I[0] == 2:
                return 2
                break
 
    # vertical wins
    if (L[0][0] == L[1][0]) and (L[0][0] == L[2][0]) == True:
        if L[0][0] == 1:
            return 1
        elif L[0][0] == 2:
            return 2
    
    elif (L[0][1] == L[1][1]) and (L[0][1] == L[2][1]) == True:
        if L[0][1] == 1:
            return 1
        elif L[0][1] == 2:
            return 2

    elif (L[0][2] == L[1][2]) and (L[0][2] == L[2][2]) == True:
        if L[0][2] == 1:
            return 1
        elif L[0][2] == 2:
            return 2
    
    # diagonal wins indexed 
    elif (L[0][0] == L[1][1]) and (L[0][0] == L[2][2]) == True:
        if L[0][0] == 1:
            return 1
        elif L[0][0] == 2:
            return 2  

    elif (L[0][2] == L[1][1]) and (L[0][2] == L[2][0]) == True:
        if L[0][2] == 1:
            return 1
        elif L[0][2] == 2:
            return 2

# PRINT BOARDS
def board(L):
    ''' Takes a ttt game as a list of lists. 
    Returns a graphical representation with 1=x, 2=o, 0=""
    '''
    print (3 * " ---")
    p0 = "|   "
    p1 = "| x "
    p2 = "| o "

    for I in L:
        for i in I:
            if i == 0:
                print(p0, end='')
            elif i == 1:
                print(p1, end='')
            elif i == 2:
                print(p2, end='')
        print("|")
        print (3 * " ---")


# SANITIZE INPUT
def san(a):   
    '''Takes the user input and checks if valid 
    (3 chars, 2 ints between 1 and 3). 
    Returns True if valid, False if not valid'''

    if len(a) != 3:
#        print("Wrong input.")
        return False
    else:
        return san_part(a[0]) and san_part(a[2])

## SANITIZE PARTIAL INPUT
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
