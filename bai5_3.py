# String Exercise - Exercise 3: Append new string in the middle of a given string
def addStr(a, b):
    la = len(a)
    mIa = 0
    if la%2 == 0:
        mIa = int(len(a)/2)
    else: 
        mIa = int(len(a)/2) +1
    print(a[:mIa]+b+a[mIa:])
addStr("Ault", "Kelly")