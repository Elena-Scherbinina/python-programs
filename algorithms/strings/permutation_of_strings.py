'''
 Permutations of a String
Generates all possible arrangements of characters in a string.
'''

def generate_permutations(s:str)->list:
    # if the string has only one character, return it as the only permutation
    if len(s) == 1:
        return [s]
    permutations=[]
    for i in range(0,len(s)):
        ch = s[i]
        # Remaining string without the current character
        remaining =s[:i] + s[i+1:]
        # Generate permutations for the remaining string
        for perm in generate_permutations(remaining):
            permutations.append(ch + perm)

    return permutations


str = "abc"
print(generate_permutations(str))


'''

If the input string has only one character, it's its own permutation.
Example: "a" → ["a"]
Recursive Case:

For each character in the string:
Treat the character as the first character of the permutation.
Find permutations of the remaining characters (recursively).
Append the character to the front of each permutation of the remainder.
Combine Results:

Gather all permutations into a list and return it.
'''