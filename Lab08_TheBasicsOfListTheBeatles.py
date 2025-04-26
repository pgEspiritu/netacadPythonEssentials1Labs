beatles = [] # step 1
print("Step 1:", beatles)

beatles.append("John Lennon") # step 2
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

for i in range(5):      # step 3
    if(i == 3):
        beatles.append("Stu Sutcliffe")
    if(i == 4):
        beatles.append("Pete Best")
print("Step 3:", beatles)

del beatles[3]    # step 4
del beatles[3]    
print("Step 4:", beatles)

beatles.insert(0, "Ringo Starr") # step 5
print("Step 5:", beatles)


# testing list legth
print("The Fab", len(beatles))

