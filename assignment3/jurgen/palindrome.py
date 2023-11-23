# def palindrome():
#     word = (input("Write a word: ")).lower()
#     for idx in range(len(word)):

#         if word[idx] != word[len(word) - 1 - idx]:
#             print("The entered string is not a palindrome")
#             return False

#     print("The entered string is a palindrome")
#     return True
            


def palindrome(word):
    result = ''
    for char in word:
        result = char + result

    if word != result:
        return False

    else:
        return True



def main():
    word = (input("Write a word: ")).lower()

    if palindrome(word) == True:
        print("The entered string is a palindrome")

    else:
        print("The entered string is not a palindrome")



            
main()





# word = 'hello world'

# result = ''
# for char in word:
#     result = char + result



# print(result)



