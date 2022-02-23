def is_palindrome (word):
    """
        Check if the word is a palindrome, based on argument passed
        Argument:
        word
    """    
    if word == word[::-1]:
        return True
    else:
        return False

