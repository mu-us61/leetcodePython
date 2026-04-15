# 268. Missing Number
# https://leetcode.com/problems/missing-number/
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a=list(range(len(nums)+1))
        for i in range(len(nums)):
            a.remove(nums[i])
        return a[0]
        
