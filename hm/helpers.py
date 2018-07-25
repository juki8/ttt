import random

def ch_word():
    ''' 
    Reads the file. Returs random word
    '''
    with open('sowpods.txt', 'r') as f:
        content = f.readlines()
        content_list = [x.strip() for x in content]

    return random.choice(content_list)

print(ch_word())
