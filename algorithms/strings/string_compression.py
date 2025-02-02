'''
String Compression and Expansion
Compresses a string by counting consecutive characters ("aaabbc" -> "a3b2c1")
or decompresses it to its original form.

compress : b2a4d5
'''

def compress(s: str) -> str:
    my_dict = {}
    for ch in s:
        if ch in my_dict:
            my_dict[ch] += 1  # Increment the count directly
        else:
            my_dict[ch] = 1  # Initialize the count

    # ''.join() for efficient string concatenation
    result = ''.join(f"{key}{value}" for key, value in my_dict.items())

    return result


def compress_my(s:str)->str:
    my_dict = {}
    for ch in s:
        if ch in my_dict:
            count = my_dict.get(ch) + 1
            my_dict[ch]= count
        else:
            my_dict[ch] = 1
            print(my_dict)
    result = ""
    for (key, value) in my_dict.items():
        result += key + str(value)

    return result

'''     
What my_dict.items() Returns:
Type: A dictionary view object.
Content: It contains tuples of key-value pairs from the dictionary, e.g., f
or {'a': 1, 'b': 2}, it would return dict_items([('a', 1), ('b', 2)]).
 
 '''
def decompress(s: str) -> str:
    result = ""
    for i in range(0, len(s), 2):  # Step by 2 to process character-number pairs
        char = s[i]
        count = int(s[i + 1])  # Get the corresponding number
        result += char * count  # Repeat the character `count` times

    return result


# Test
print(compress("bbaaaaddddd"))  # "b2a4d5"
print(compress("abc"))          # "a1b1c1"

compressed_string = "a3b1c4"
print(f"Decompressed: {decompress(compressed_string)}")
