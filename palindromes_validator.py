def palindrome(word):
    word = word.replace(" ", "")
    word = word.lower()
    word_invert = word[::-1]
    if word == word_invert:
        return True
    else:
        return False

main = """
Hello!, enter a word, sentence or number to comprobate if is a palindrome..

Note: A palindrome is a word, sentence or number that it read alike from left to right.

Example: Ana

Write your datum: """        


def run():
    word = input(main)
    is_palindrome = palindrome(word)
    if is_palindrome == True:
        print("Yes!, Is a palindrome")
    else:
        print("No!, is not palindrome")    


if __name__ == "__main__":
    run()