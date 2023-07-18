# Dictionary Exercise - Exercise 4: Initialize dictionary with default values
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
a = dict()
for x in employees:
    a[x] = defaults
print(a)