#7. Division Calculator
#Accept two numbers from the user and perform division.
#Handle:
#- Invalid input
#- Division by zero
try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Result =", a / b)
except ValueError:
    print("Invalid input, enter numbers only")
except ZeroDivisionError:
    print("Cannot divide by zero")