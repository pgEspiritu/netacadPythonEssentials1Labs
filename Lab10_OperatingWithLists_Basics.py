my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

new_myList = []
for i in my_list:
    if i not in new_myList:
        new_myList.append(i)

print(new_myList)

print("The list with unique elements only:")
print(my_list)

