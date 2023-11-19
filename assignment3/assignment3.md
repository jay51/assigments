## Python assignment 3

### Problem 1: Palindrome Checker

**Write a Python program that checks whether a given string is a palindrome or not.
A palindrome is a word, phrase, or sequence that reads the same backward as forward.**

### Steps:

- Prompt the user to enter a string.
- Write a function that takes a string as input and returns True if it is a palindrome and False otherwise.
- Ensure the comparison is case-insensitive, i.e., 'Racecar' should be considered a palindrome.
- Print a message indicating whether the entered string is a palindrome or not.

Example:
```py
Enter a string: racecar
Output: The entered string is a palindrome.

Enter a string: hello
Output: The entered string is not a palindrome.
```

## Python assignment 3
### Problem 2: Number Guessing Game

**Implement a simple number guessing game in Python. The program should generate a random number between 1 and 100,
allow the user to guess the number, and provide feedback on whether the guess is too high, too low, or correct.**
### Steps:

- Use the random module to generate a random number between 1 and 100.
- Prompt the user to guess the number.
- Compare the user's guess with the randomly generated number.
- Provide feedback to the user, indicating whether the guess is too high, too low, or correct    Repeat or End:
- If the guess is incorrect, allow the user to guess again.
- Continue the process until the user correctly guesses the number.
- Print a congratulatory message when the correct number is guessed.

Example:
```py
Welcome to the Number Guessing Game!
Guess the number between 1 and 100.

Enter your guess: 50
Too low. Try again.

Enter your guess: 75
Too high. Try again.

Enter your guess: 63
Congratulations! You guessed the correct number (63).
```
