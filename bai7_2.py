# List Exercise - Exercise 2: Concatenate two lists index-wise
def cList(a, b):
    c = list()
    for x in range(0, len(a), 1):
        c.append(a[x] + b[x])
    print(c)
       
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"] 
cList(list1, list2)