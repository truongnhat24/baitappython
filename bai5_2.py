# String Exercise - Exercise 2: Create a string made of the middle three characters
str1, str2 = "JhonDipPeta", "JaSonAy"
def threecharacter(s):
    mI = int(len(s)/2)
    print(s[mI-1], s[mI], s[mI+1])
    print("")
threecharacter(str1)
threecharacter(str2)