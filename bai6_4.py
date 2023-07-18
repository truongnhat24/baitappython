# Data Structure Exercise - Exercise 4: Count the occurrence of each element from a list
def countArr(a):
    d = dict()
    la = len(a)
    for x in a:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    print(d)
        
    
countArr([11, 45, 8, 11, 23, 45, 23, 45, 89])