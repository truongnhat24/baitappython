# Functions Exercise - Exercise 2: Create a function with variable length of arguments
def func1(*args):
    for x in args:
        print(x)
func1(1, "a", 2)