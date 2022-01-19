"""
Emmy Veselinov
Project: Calculator
"""
import random

def add(number1, number2):
    result = number1 + number2
    return result

def subtract(number1, number2):
    result = number1 - number2
    return result

def divide(number1, number2):
    result = number1/number2
    return result

def multiply(number1, number2):
    result = number1 * number2
    return result


def calculate(num1, num2, typeofcalc):
    choices = ["A", "S", "D", "M"]
    if typeofcalc in choices:
        if typeofcalc == "A":
            result = str(num1), "+", str(num2), "=", str(add(num1, num2)), " Answer: ", str(add(num1, num2))
        elif typeofcalc == "S":
            result = str(num1), "-", str(num2), "=", str(subtract(num1, num2)), " Answer: ", str(subtract(num1, num2))
        elif typeofcalc == "D":
            result = str(num1), "%", str(num2), "=", str(divide(num1, num2)), " Answer: ", str(divide(num1, num2))
        elif typeofcalc == "M":
            result = str(num1), "*", str(num2), "=", str(multiply(num1, num2)), " Answer: ", str(multiply(num1, num2))
    else:
        result = "Choice of calculation not found"
        
    return "".join(result)

if __name__ == "__main__":
    print("Welcome!")
    print("A: Add")
    print("S: Subtract")
    print("D: Divide")
    print("M: Multiply")
    while True:
        typeofcalc = input("Enter your choice of calculation(A/S/D/M): ")
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print(calculate(num1, num2, typeofcalc))
        nextcalc = input("Would you like to do another calculation? (Yes/No) ")
        if nextcalc == "No":
            greetings = ["Have a nice day!", "Thank you for using the calculator!", "See you next time!", "Farewell!", "Goodbye!"]
            print(random.choice(greetings))
            break
    
