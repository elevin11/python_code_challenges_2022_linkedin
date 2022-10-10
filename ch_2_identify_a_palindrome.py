

def is_palindrome(word):
    if len(word) <= 1:
        return True
    elif not word[0].isalpha():
        return is_palindrome(word[1:])
    elif not word[-1].isalpha():
        return is_palindrome(word[:-1])
    elif word[0].lower() == word[-1].lower():
        return is_palindrome(word[1:-1])
    else:
        return False


while (True):
    word_in = input("Enter a word: ")
    if is_palindrome(word_in):
        print(f"{word_in} is a palindrome!")
    else:
        print(f"{word_in} is not a palindrome")
