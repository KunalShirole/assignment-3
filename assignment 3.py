# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


lis = [2, 1, 3, 5, 4, 3, 8]
print ("List elements are : ", end="")
for i in range(0, len(lis)):
    print(lis[i], end=" ")

lis.pop(2)
print ("List elements after popping are : ", end="")
for i in range(0, len(lis)):
    print(lis[i], end=" ")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
