
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

#    else: 
#        print("no winner")


#    # horizontal wins
#    winner_a = (a1 == a2) and (a1 == a3)
#    winner_b = (b1 == b2) and (b1 == b3)
#    winner_c = (c1 == c2) and (c1 == c3)
#    
#    # horizontal wins indexed
#    winner_a = (A[0] == A[1]) and (A[0] == A[2])
#    winner_b = (B[0] == B[1]) and (B[0] == B[2])
#    winner_c = (C[0] == C[1]) and (C[0] == C[2])    
#    
#    # vertical wins
#    winner_1 = (a1 == b1) and (a1 == c1)
#    winner_2 = (a2 == b2) and (a2 == c2)
#    winner_3 = (a3 == b3) and (a3 == c3)
#
#    # vertical wins indexed
#    winner_1 = (L[0][0] == L[1][0]) and (L[0][0] == L[2][0])
#    winner_2 = (L[0][1] == L[1][1]) and (L[0][1] == L[2][1])
#    winner_3 = (L[0][2] == L[1][2]) and (L[0][2] == L[2][2])
#
#    # diagonal wins
#    winner_d1 = (a1 == b2) and (a1 == c3)
#    winner_d2 = (a3 == b2) and (a3 == c1)
#
#    # diagonal wins indexed 
#    winner_d1 = (L[0][0] == L[1][1]) and (L[0][0] == L[2][2])
#    winner_d2 = (L[0][2]] == L[1][1]) and (L[0][2] == L[2][0])
