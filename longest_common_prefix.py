from typing import List



def longestCommonPrefix(strs: List[str]) -> str:
    minimal = min(len(ele) for ele in strs)

    res = ""
    d = []
    for i in range(minimal):
        d.append(set())
        for word in strs:
            d[i].add(word[i])
        if len(d[i]) == 1:
            res += d[i].pop()
        else:
            break

    return res

a = longestCommonPrefix(["flower","flow","flight"])

print(a)