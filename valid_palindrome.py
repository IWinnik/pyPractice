import re

regex = re.compile('[^a-z0-9]')


def isPalindrome( s: str) -> bool:
    lowered = s.lower()
    s = regex.sub('', lowered)
    print(s)
    l = list(s)
    print(l)

    l2 = list(reversed(l))

    print(l2)
    return l == l2

s = "A man, a plan, a canal: Panama"

print(isPalindrome(s))