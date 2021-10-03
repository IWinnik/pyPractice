def firstUniqChar(s: str) -> int:
    temp_s = s
    unique_founded = 0
    while len(temp_s) > 0:
        unique = temp_s[0]
        if s.count(unique) > 1:
            temp_s = temp_s.replace(unique, '')
        else:
            unique_founded = 1
            break

    if unique_founded == 0:
        return -1
    return s.index(unique)


s = "aabb"
s2 = "loveleetcode"

print(firstUniqChar(s))
print(firstUniqChar(s2))
