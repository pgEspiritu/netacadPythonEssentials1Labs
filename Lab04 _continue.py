userInput = input("Enter a word: ")     # Prompt the user to enter a word
user_word = userInput.upper()           # and assign it to the user_word variable.


for letter in user_word:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        print(letter)