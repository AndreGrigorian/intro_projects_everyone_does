"""Performs simple arthimetic on two  numbers."""

import math

def addition():
   print("------Addition-----")
   num1 = int(input("Enter first value: "))
   num2 = int(input("Enter second value: "))
   print(f"{num1} + {num2} = {num1 + num2}")

def subtraction():
   print("------Subtraction-----")
   num1 = int(input("Enter first value: "))
   num2 = int(input("Enter second value: "))
   print(f"{num1} - {num2} = {num1 - num2}")

def multiplication():
   print("------Multiplication-----")
   num1 = int(input("Enter first value: "))
   num2 = int(input("Enter second value: "))
   print(f"{num1} * {num2} = {num1 * num2}")

def division():
   print("------Division-----")
   num1 = int(input("Enter first value: "))
   num2 = int(input("Enter second value: "))
   print(f"{num1}/{num2} = {num1 / num2}")

def pow():
   print("------Power-----")
   num1 = int(input("Enter first value: "))
   num2 = int(input("Enter second value: "))
   print(f"{num1}^{num2} = {num1 ** num2}")

def sqrt():
   print("------Square Root-----")
   num1 = int(input("Enter value: "))
   print(f"sqrt({num1}) = {math.sqrt(num1)}")

#recursively find factorial
def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num-1)

def main():
    print("------Options-----\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Powers\n6. Square Root\n7. Factorial\n8. Quit")
    try:
        choice = int(input("Enter Option #: "))
    except:
        print("Invalid Entry.")
    
    while choice != 8:

        if choice == 1:
            addition()
        elif choice == 2:
            subtraction()  
        elif choice == 3:
            multiplication()  
        elif choice == 4:
            division()
        elif choice == 5:
            pow()
        elif choice == 6:
            sqrt()
        elif choice == 7:
            print("------Factorial-----")
            num1 = int(input("Enter value: "))
            print(f"factorial of {num1} = {factorial(num1)}")
        else:
            print("Please enter a valid option number")
        
        try:
            choice = int(input("Enter Option #: "))
        except:
            print("Invalid Entry.")
    
    print("Goodbye!")


if __name__ == '__main__':
    main()