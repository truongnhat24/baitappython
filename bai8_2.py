# Dictionary Exercise - Exercise 2: Merge two Python dictionaries into one
def mDict(a, b):
    c = dict()
    c.update(a)
    c.update(b)
    print(c)
       
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
mDict(dict1, dict2)