'''
String Rotation Check
Determines if one string is a rotation of another (e.g., "abc" and "bca").
'''

def check_rotation(s1:str, s2:str)->bool:
    if len(s1) != len(s2):
        return False
    for i in range(0,len(s1)+1):
        s = s1[i:] + s1[0:i]
        print(s + "\n")
        if s == s2:
            return True
    return False

'''
Optimized
'''
def check_rotation2(s1: str, s2: str) -> bool:
    # Check if lengths are the same
    if len(s1) != len(s2):
        return False

    # Check if s1 is a substring of s2 concatenated with itself
    return s1 in (s2 + s2)


s1 = "abcs"
s2 = "bcsa"
print(check_rotation2(s1, s2))