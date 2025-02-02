'''
generate all subsequences of a string
A subsequence of a string is a new string generated from the original string
by deleting zero or more characters without changing the relative order
of the remaining characters.


Key Points:
Order matters: The characters in the subsequence must appear in the same order as in the original string.
Characters can be skipped: You can choose to include or exclude each character, but you can't rearrange them.
Empty subsequence: An empty subsequence is always valid, as you can exclude all characters.
Example:
For the string "abc":

Subsequences include:
"", "a", "b", "c", "ab", "ac", "bc", "abc"

Total Number of Subsequences:
For a string of length n, there are
2 power n   possible subsequences (including the empty string).
  This is because each character has two choices: either it is included or excluded.
  For example:

Length of "abc" = 3
Total subsequences =   2 power 3 = 8
["","a","b","c", "ab","ac","bc","abc"]
'''


def generate_subsequences(s: str) -> list:
    # Start with an empty list containing an empty string
    subsequences = [""]
    print("subsequences = [""]")

    # Loop through each character in the string
    for char in s:
        print(f"char : {char}")
        # Create new subsequences by appending the current character to each existing subsequence
        new_subsequences = [sub + char for sub in subsequences]
        print(f"new_subsequences = [sub + char for sub in subsequences])] : {new_subsequences}")

        # Add the new subsequences to the existing ones
        subsequences.extend(new_subsequences)
        print(f"subsequences.extend(new_subsequences) : {subsequences}")
        print("******************************************")

    return subsequences


# Example usage
string = "abc"
print("**--**--**--**--**--**--**-**--**")
print(f"Subsequences of '{string}': {generate_subsequences(string)}")
