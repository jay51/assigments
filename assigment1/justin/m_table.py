"""
Task 3: Multiplication Table
Create a Python program that does the following:
Ask the user to input a number.
Generate & display the multiplication table for that number from 0 to 10.
example:
    1 x 0 = 0
    1 x 1 = 1
    1 x 2 = 2
    1 x 3 = 3
    1 x 4 = 4
    ...
"""


def multiply(num):
    for idx in range(11):
        result = num * idx
        print(f"{num} x {idx} = {result}.")




def main():
    num = int(input("Enter numer, no decimals."))
    multiply(num)

main()
