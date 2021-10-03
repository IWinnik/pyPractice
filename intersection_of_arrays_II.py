from collections import Counter
from typing import List


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    dic1 = Counter(nums1)
    res = []
    for n in nums2:
        if n in dic1 and dic1[n] > 0:
            res.append(n)
            dic1[n] -= 1
    return res

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

print(intersect(nums1, nums2))