
'''
Shift Characters
Adjusts the position of each character in a string by a fixed amount,
often used in encryption like Caesar cipher.

Shift by 1 to the right:
Each character is moved one position forward in the alphabet:
a -> b, b -> c, c -> d
Result: "bcd"

Key Points:
Wrap Around:
If the character goes past z (or before a), it wraps around the alphabet (circular shift).

Case Sensitivity:
Shifts usually treat uppercase (A-Z) and lowercase (a-z) letters separately.

Non-Alphabet Characters:
Often, spaces, punctuation, and numbers are left unchanged.
'''

import string

def shift_characters(s:str, k):
    shift_base = 0
    result = ""
    for ch in s:
        if ch.isalpha():
            if ch.isupper():
                shift_base = ord('A')
            elif ch.islower():
                shift_base = ord('a')

            new_char =chr((ord(ch) - shift_base +k)%26 + shift_base)
            result += new_char
        else:
            result += ch
    return result

def shift_characters2(s, shift):
    result = ""
    for char in s:
        if char.isalpha():  # Only shift alphabetic characters
            shift_base = ord('A') if char.isupper() else ord('a')
            # Compute the new position with wrapping
            new_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            result += new_char
        else:
            result += char  # Leave non-alphabetic characters unchanged
    return result

# Test cases
print(shift_characters("abc", 1))          # "bcd"
print(shift_characters("xyz", 3))          # "abc" (wraps around)
print(shift_characters("Hello, World!", 5))  # "Mjqqt, Btwqi!"



my_string = "ABC"
print(shift_characters(my_string, 2))


'''
Explanation of Code:
ord(): Converts a character to its Unicode (ASCII) value.
Example: ord('a') = 97, ord('z') = 122.

Shifting:

Subtract the base (ord('a') or ord('A')) to work within 0-25 range.
Add the shift amount, take modulo 26 (to handle wrapping), and add back the base.
chr(): Converts a Unicode value back to a character.
Example: chr(97) = 'a'.'''


