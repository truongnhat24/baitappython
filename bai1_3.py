# Basic Exercise for Beginners - Exercise 3: Print characters from a string that are present at an even index number
n = input("Input string: ")
for x in range(0, len(n), 1):
    if x % 2 == 0:
        print(n[x])