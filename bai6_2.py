# Data Structure Exercise - Exercise 2: Remove and add item in a list
def removeandadd(a):
    i = a[4]
    a.remove(a[4])
    a.insert(2, i)
    a.append(i)
    print(a)
list1 = [54, 44, 27, 79, 91, 41]
removeandadd(list1)