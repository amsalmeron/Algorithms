"""
169. Majority Element
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
"""
from collections import Counter
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # if not nums:
        #     return 0

        # max = 0
        # target = 0
        # sorted_nums = sorted(nums)
        # unique_nums = list(set(nums))
        # for i in unique_nums:
        #     total_count = sorted_nums.count(i)
        #     if total_count > max:
        #         max = total_count
        #         target = i
        # return target

        # Count occurrences of each element
        counts = Counter(nums)
        # Find the element with the maximum count
        return max(counts, key=counts.get)
