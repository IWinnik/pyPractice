
def strStr(haystack: str, needle: str) -> int:
    if len(needle) == 0:
        return 0
    if needle not in haystack:
        return -1
    return haystack.index(needle)

a = strStr("Ireneusz","neu")

print(a)