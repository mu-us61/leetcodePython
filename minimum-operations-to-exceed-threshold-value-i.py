# https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-i/
# 3065


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        result=0
        for i in nums:
            if i < k:
                result += 1
            else:
                break
        return result
        
