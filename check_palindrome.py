def is_palindrome(word):
    # Ignore Case
    word = word.lower()
    for i in range(0, len(word)//2):
        if word[i] != word[len(word)-i-1]:
            return False
    return True


# Driver Code
word = input("Enter a word to check Palindrome:")
if __name__ == '__main__':
    palindrome = is_palindrome(word)
    if palindrome:
        print("Given word is palindrome")
    else:
        print("Not a Palindrome")