# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/description/
# 1464
class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        nums.sort()

        return (nums[-1]-1)*(nums[-2]-1)
