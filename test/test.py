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


L = [[2, 2, 0],	[2, 1, 0], [2, 1, 1]]
board(L)


#     if L[0][0] == 0:
#         a = "|   "
#     elif L[0][0] == 1:
#         a = "| x "
#     elif L[0][0] == 2:
#         a = "| o "
    
#     if 


#     print ("| ")




# row = 3
# column = 3

# # Row: Horizontal bars function
# def createVer():
#     return row * " ---"

# # Row: Vertical bars function
# def createHor():
#     return row * "|   " + "|"

# # Calls funtions for each column
# for _ in range(column):
#     print(createVer())
#     print(createHor())

# # End vertical bars
# print(createVer())