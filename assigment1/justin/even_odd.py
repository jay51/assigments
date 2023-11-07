"""""
Task 2: Even or Odd
Create a Python program that does the following:
Ask the user to input a number.
Check if the number is even or odd.
Display a message to the user indicating whether the number is even or odd.
"""

def even_odd(num):
    if num % 2 == 0:
        print(f"number you've entered, {num} is even.")
    else:
        print(f"number you've entered, {num} is odd.")


def main():
    num = int(input("Enter a whole, no decimals, number. "))
    even_odd(num)


main()
