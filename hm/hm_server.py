from helpers import ch_word, print_word, check_letter, suc
## GAME SETTINGS

word = ch_word()
guessed = []
guesses = 0

## TESTING
print(word)

## GAME 
print("Start game!")
while True: 

    a = input("Please choose a letter!: ").upper()
    guesses += 1
    print(a)

    if a == 'EXIT':
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

        # Check if match is over
        word_short = "".join(set(word))
        print(len(word))
        print(len(word_short))
        print(len(guessed))
        if len(word_short) == len(guessed):
            print("Success! with " + str(guesses) + " guesses.")
            break

    else:
        print("Letter not in word. ")       