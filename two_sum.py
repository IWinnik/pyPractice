class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for num in nums:
            rest = target - num
            try:
                idx = nums.index(rest, nums.index(num) + 1)
            except:
                idx = -1
            if idx > -1:
                return [nums.index(num), idx]
                break



