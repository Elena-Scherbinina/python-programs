'''
Checks whether a string or sequence reads the same backward as forward.
'''

def is_palindrome(s):
    s = s.replace(" ","").lower()

    return s == s[::-1]


print(f" is palindrome() : {is_palindrome("Tasat")}")