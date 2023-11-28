import random

def main():

    print("""Wellcome to the Number Guessing Game!
    Guess the number between 1 and 100 in 6 tries
    """)

    random_number = random.randint(0, 101)
    tries = 6

    while True:
        
        your_guess = int(input("Enter your guess: "))
        tries -= 1

        if tries == 0:
            print(f"{tries} tries left \n Game Over")
            break

        elif your_guess == random_number:
            print(f"You guessed the correct number {random_number}")
            break
        
        elif your_guess < random_number:
            print("Too low, Try again")
            print(f"{tries} tries left")

        elif your_guess > random_number:
            print("Too high, Try again")
            print(f"{tries} tries left")

main()