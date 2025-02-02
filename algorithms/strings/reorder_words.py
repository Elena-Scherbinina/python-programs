'''
Reverses the order of words in a sentence without altering the characters
within each word (e.g., "Hello World" becomes "World Hello").
'''



def reverse(sentence:str):
    words = sentence.split()
    new_words = words[::-1]
    return " ".join(new_words)

s = "I like to dance"
print(f"reverse : {reverse(s)}")
