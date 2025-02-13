# https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i
# 3264. Final Array State After K Multiplication Operations I

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            minnumber=min(nums)
            index=nums.index(minnumber)
            nums[index]=minnumber*multiplier
        return nums
        
