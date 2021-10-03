from typing import List


def reverseString(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    s.reverse()


def reverseString2(s: List[str]) -> None:
    i = 0
    j = len(s) - 1

    while i <= j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1

s = ["H","a","n","n","a","h"]


reverseString(s)
print(''.join(s))
reverseString2(s)
print(''.join(s))
