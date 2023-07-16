# String Exercise - Exercise 3: Create a new string made of the first, middle, and last characters of each input string
def strC(a, b):
    mA = int(len(a)/2)
    mB = int(len(b)/2)
    print(a[0] + b[0] + a[mA] + b[mB] + a[len(a)-1] + b[len(b)-1])
strC("America", "Japan")