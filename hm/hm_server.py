from helpers import ch_word, print_word, check_letter
## GAME SETTINGS

word = ch_word()
guessed = []
guesses = 0

## TESTING
print(word)

## GAME 
print("Start game!")
while True: 

    if len(guessed) == len(word):
        print("Success! with " + str(guesses) + " guesses.")
        break

    a = input("Please choose a letter!: ").upper()
    guesses += 1
    print(a)

    if a == 'exit':
        break

    # Checks if input is correct 
    a_checked = check_letter(a, word)
    print (a_checked)

    if a_checked == False:
        print("Incorrect input. Please type one letter only. ")

    elif a_checked == True:
        print("Correct!")
        guessed.append(a)
        print(guessed)
        print_word(word, guessed)

    else:
        print("Letter not in word. ")