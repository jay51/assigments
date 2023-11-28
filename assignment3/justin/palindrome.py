def is_palindrome(user_input):
    print(f"What you've entered {user_input} IS a palindrome.")
    
def not_palindrome(user_input):
    print(f"What you've entered {user_input} is NOT a palindrome.")

def palindrome(user_input, user_input_length):

    for idx in range(user_input_length):

        if user_input[idx] != user_input[user_input_length - 1]:

            not_palindrome(user_input)
            return

        user_input_length -= 1

    is_palindrome(user_input)

def main():
    user_input = input("Enter a word or a phrase. ").upper()
    user_input_length = len(user_input)


    print(f"What the user entered is {user_input} and the length is {user_input_length}.")
    palindrome(user_input, user_input_length)

main()