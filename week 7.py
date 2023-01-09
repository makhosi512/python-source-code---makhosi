print("palindrome checker program")
print()
word = input(f"please enter a word: ")
print()
def is_palindrome(word):
    if(word==word[::-1]):
        print(f"{word} is a palindrome")
    else:
        print(f"{word} is not a palindrome")
        
is_palindrome(word)        