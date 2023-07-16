# Functions Exercise - Exercise 4: Create a function with a default argument
def show_employee(a, b = "9000"):
    print("Name: ", a, ", salary: ", b)
    
m = input("Nhap a: ")
n = input("Nhap b: ")
show_employee(m,n) if (n != "") else show_employee(m)