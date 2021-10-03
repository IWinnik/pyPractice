def isAnagram( s: str, t: str) -> bool:
    s = list(s)
    t = list(t)
    s.sort()
    t.sort()
    return True if s == t else False


s = "anagram"
t = "nagaram"

print(isAnagram(s,t))