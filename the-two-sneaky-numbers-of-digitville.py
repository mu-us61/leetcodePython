# https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description/
# 3289. The Two Sneaky Numbers of Digitville

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        real = list(set(nums))
        for i in real:
            nums.remove(i)
        return nums
