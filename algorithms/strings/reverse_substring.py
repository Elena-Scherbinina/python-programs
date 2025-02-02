'''
    Reverse Substring
    Reverses a specified portion of a string or array instead of the entire sequence.
'''

def reverse_part_string(s:str, start:int,end:int)->str:
    if start > end or start < 0 or end > len(s):
        raise ValueError("Invalid start or end indices")

    # Slice the string into three parts
    prefix = s[:start]      # Part before the reversed section, start not included
    to_reverse = s[start:end+1]
    suffix = s[end+1:]      # The portion to reverse
    return prefix + to_reverse[::-1] + suffix   # Part after the reversed section

def process(s:str, start:int, end:int):
    my_substr = s[start:end+1]
    part1 = s[0:start]
    part2 = my_substr[::-1]
    print(part2 +"\n")
    part3 = s[end+1:]
    return part1 + part2 +part3

my_string = "My Python class"
print(reverse_part_string(my_string, 3,8))

#print(process(my_string, 3,8))