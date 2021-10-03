nums = [1,2]
k = 6


def rotate(nums, k):
    """

    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    l = len(nums)
    if k > l:
        k = k % l
    nums[:] = nums[l-k:] + nums[:l-k]

rotate(nums, k)
print(nums)