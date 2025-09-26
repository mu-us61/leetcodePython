# 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = []  # track what we have seen
        i = 0
        while i < len(nums):   # use while since list length changes
            if nums[i] in unique:
                del nums[i]   # remove duplicate
            else:
                unique.append(nums[i])
                i += 1        # only move forward when not deleting
        return len(nums)
