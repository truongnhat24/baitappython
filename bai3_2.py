# Loop Exercise - Exercise 2: Print the following pattern
n = int(input("Nhap so hang cot: "))
for x in range(1, n+1, 1):
    for y in range(1, x+1):
        print(y, end=" ")
    print("")