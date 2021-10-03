from typing import List


def singleNumber(nums: List[int]) -> int:
    nums.sort()
    counter = 1
    last_el = nums[0]
    for num in nums[1:]:
        if num == last_el:
            counter += 1
        elif counter == 1:
            return last_el
        else:
            counter = 1

        last_el = num
    return nums[-1]

nums = [4,1,2,1,2]

print(singleNumber(nums))