# https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements
# 3194

class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        avg=[]
        for _ in range(len(nums)//2):
            avg.append((min(nums)+max(nums))/2)
            nums.remove(min(nums))
            nums.remove(max(nums))
        return min(avg)
