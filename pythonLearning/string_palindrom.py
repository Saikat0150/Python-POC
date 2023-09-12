def is_palindrome(word):
    reversed_word = word[::-1]
    return word == reversed_word


word = input("Enter the word to check: ")
result = is_palindrome(word)
if result:
    print("The word is palindrome..")
else:
    print("The word is not palindrome..")