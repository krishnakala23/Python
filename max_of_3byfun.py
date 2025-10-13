def find_max(a, b, c):
    return max(a, b, c)
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

maximum = find_max(num1, num2, num3)
print(f"The maximum of the three numbers is: {maximum}")
