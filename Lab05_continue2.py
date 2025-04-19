word_without_vowels = ""

x = input("Enter a Word: ")
user_word = x.upper()

for letter in user_word:
    if (letter == "A"):
        continue
    elif (letter == "E"):
        continue
    elif (letter == "I"):
        continue
    elif (letter == "O"):
        continue
    elif (letter == "U"):
        continue
    else:
        word_without_vowels += letter

print(word_without_vowels) # Print the word assigned to word_without_vowels.

