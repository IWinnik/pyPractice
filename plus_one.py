from typing import List


def plusOne( digits: List[int]) -> List[int]:

    right = len(digits) - 1

    while right >= 0:
        if digits[right] != 9:
            digits[right] += 1
            return digits
        digits[right] = 0
        right -= 1
    # edge case if all 9's then add 1 in front
    return [1] + digits


digits = [4,3,2,1]

print(plusOne(digits))