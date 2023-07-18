# Dictionary Exercise - Exercise 1: Convert two lists into a dictionary
def cDict(a, b):
    c = dict()
    for x in range(0, len(a), 1):
        c[a[x]] = b[x]
    print(c)
       
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
cDict(keys, values)