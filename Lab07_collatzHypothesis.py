number = int(input("Enter a valid number: "))

while(number <= 0):                                 #Check the input (must be greater than 0)
    print("Error: Input a valid number")
    number = int(input("Enter a valid number: "))

c0 = number
steps = 0

while(c0!=1):
    if(c0%2==0):
        c0 = c0 / 2
    else:
        c0 = 3 * c0 + 1
    print(int(c0))
    steps += 1
print("steps = " + str(steps))