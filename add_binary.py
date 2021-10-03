from typing import List


def plusOne( digits: List[int]) -> List[int]:
    j = len(digits) - 1

    while j >= 0:
        if digits[j] != 9:
            digits[j] += 1
            return digits
        digits[j] = 0
        j -= 1

    return [1] + digits

print(plusOne([1,2,9]))