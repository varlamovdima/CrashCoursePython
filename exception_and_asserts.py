try:
    array = [1,2,3,4]
    print(array[5])
except IndexError:
    print("Index 5 does not exist!")
except:
    print("All other exceptions go here!")
else:
    print("No indexing problems!")
finally:
    print("This will print in any case!")

try:
    print(arrat)
except NameError:
    print("That variable doesn't exist!")

try:
    print(7/"20")
except TypeError:
    print("You can't divide an integer by a string!")

try:
    bad_file = open("does_not_exist.txt","r")
except IOError:
    print("Can not find that file!")

try:
    array = [1,2,3]
    array.appenf(4)
except AttributeError:
    print("We meant to use .append()")

try:
    print(int("This can't be an int!"))
except ValueError:
    print("Casting a string to a int doesn't work!")

try:
    print(10/0)
except:
    print("Division by zero is not defined")
    #raise ZeroDivisionError("We can't divide 10 by 0!")

grades = []
assert len(grades) !=0, "List of grades is empty!"
average = sum(grades)/len(grades)

