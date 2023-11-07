""""
Task 1: Simple Calculator
Create a Python program that does the following:
Ask the user to input two numbers.
Ask the user to choose an operation (addition, subtraction, multiplication, or division) using a menu.
Perform the chosen operation on the two numbers.
Display the result to the user.
"""



def display(operation, num1, num2, result):
    ops = {'A': 'ADD', 'S': 'SUBTRACT', 'M': 'MULTIPLY', 'D': 'DIVIDE'}
    op = ops[operation]

    print(f"DISPLAY = The numbers you entered are {num1} and {num2} you chose to {op}, and the result is {result}.")


def calc(num1, num2):

    operation = input("What math operation do you choose; 'A' = add, 'S' = subtract, 'M' = multiply, 'D' = divide, and 'Q' = quit?. ").upper()
    if operation == "A":
        result = num1 + num2
        display(operation, num1, num2, result)
    elif operation == "S":
        result = (num1 - num2)
        display(operation, num1, num2, result)
    elif operation == "M":
        result = (num1 * num2)
        display(operation, num1, num2, result)
    elif operation == "D":
        result = (num1 / num2)
        display(operation, num1, num2, result)
    elif operation == "Q":
        print("You chose to quit the game. G-bye.")
    else: 
        print("You entered an invalid choice.")



def main():
    num1 = input("Enter a number.\n")
    num2 = input("Enter a number.\n")

    calc(int(num1), int(num2))



main()
