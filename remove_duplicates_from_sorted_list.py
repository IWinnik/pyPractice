def removeDuplicates(nums_internal):
    """
    :type nums: List[int]
    :rtype: int
    """
    global nums
    nums = list(set(nums_internal))
    return len(nums)


nums = [i for i in range(10)]
nums2 = nums
print(nums2)
