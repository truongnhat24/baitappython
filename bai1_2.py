# Basic Exercise for Beginners - Exercise 2: Print the sum of the current number and the previous number
sum = pre = 0
for x in range(0, 10, 1):
  print("previous number: ", pre, ", current number: ", x, ", sum: ", pre+x)
  pre = x