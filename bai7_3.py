# List Exercise - Exercise 3: Turn every item of a list into its square
def sList(a):
    b = list()
    for x in range(0, len(a), 1):
        b.append(a[x]*a[x])
    print(b)
       
list1 = [1, 2, 3, 4, 5, 6, 7]
sList(list1)