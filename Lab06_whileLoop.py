blocks = int(input("Enter the number of blocks: "))

height = 0
cl = 0           #current layer
nl = 1           #next layer

while (blocks >= nl):
    blocks -= nl
    height += 1
    nl += 1
    
print("The height of the pyramid:", height)

