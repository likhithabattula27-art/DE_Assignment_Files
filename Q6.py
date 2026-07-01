#6. Exception Handling
#Write a program that accepts a number from the user and handles invalid input using try-except.
#Example:
#python Enter a number: abc Invalid Input
try:
    num = int(input("Enter a number: "))
    print("You entered", num)
except:
    print("Invalid Input")
    