# Data Structure Exercise - Exercise 1: Create a list by picking an odd-index items from the first list and even index items from the second
def oddeven(a, b):
    c = []
    for x in range(0, len(a), 1):
        if x%2 !=0:
            c.append(a[x])
    for y in range(0, len(b), 1):
        if y%2 == 0:
            c.append(b[y])
    print(c)
l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
oddeven(l1, l2)