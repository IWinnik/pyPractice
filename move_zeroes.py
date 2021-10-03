from typing import List


def moveZeroes( nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    nums2 = [item for item in nums if item != 0]
    zeros = [item for item in nums if item == 0]
    # print(nums2)

    nums[:] = nums2 + zeros


nums = [0,1,0,3,12]
moveZeroes(nums)

print(nums)