# List Exercise - Exercise 4: Concatenate two lists in the following order
def tList(a, b):
    c = list()
    for x in range(0, len(a), 1):
        for y in range(0, len(b), 1):
            c.append(a[x] + b[y])
    print(c)
       
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
tList(list1, list2)