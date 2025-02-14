# https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target
# 2824

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        n=len(nums)
        out=0
        for i in range(n):
            for j in range(i+1,n):
                if (nums[i] + nums[j]) < target:
                    out+=1
        return out
