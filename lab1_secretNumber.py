secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

number = 0           #initial value

while (number != 777):
    number = int(input("Guess the number: "))
    print("Ha ha! You\'re stuck in my loop!")
    
print("Well done, muggle! You are free now.")
