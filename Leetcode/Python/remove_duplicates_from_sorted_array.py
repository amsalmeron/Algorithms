"""
26. Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
"""
    
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # check if nums exists
        if not nums:
            return 0

        # declare k at 1 becuse first index always unqiue
        k = 1

        # start iterating from index 1 to lendgeth of nums
        for i in range(1, len(nums)):
            # if current number is not the same as the previous, place in nums
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
        return k