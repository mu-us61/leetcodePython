# 169
# https://leetcode.com/problems/majority-element

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        border=len(nums)//2
        # count=0
        # for i in range(len(nums)):
        #     for j in nums:
        #         if nums[i] == j:
        #             count=count+1
        #     if count >= border +1:
        #         return nums[i]
        #     else:
        #         count=0
        unique_items=set(nums)
        for i in unique_items:
            if nums.count(i)>border:
                return i
