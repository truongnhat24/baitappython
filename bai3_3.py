# Loop Exercise - Exercise 3: Calculate the sum of all numbers from 1 to a given number
n = int(input("nhap n: "))
sum = 0
for x in range(1, n+1, 1):
    sum += x
print(sum)