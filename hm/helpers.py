import random

# Choose word from list
def ch_word():
    ''' 
    Reads the file. 
    Returs random word.
    '''
    with open('sowpods.txt', 'r') as f:
        content = f.readlines()
        content_list = [x.strip() for x in content]

    return random.choice(content_list)

# Check if input letter is in word
def check_letter(a, word):
    '''
    Checks if input contains one letter.
    Checks if letter in word.
    Returns True or False
    '''
    if len(a) != 1:
        return False

    if a in word:
        return True

# Print word with guessed letter
def print_word(word, guessed):
    '''
    Prints word with guessed letters
    '''
    for l in word:
        if l in guessed:
            print (" " + str(l.upper()) + " ", end = "")
        else:
            print (" _ ", end = "")
    print("\n")