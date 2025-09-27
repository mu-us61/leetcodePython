#  27
# https://leetcode.com/problems/remove-element/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        a=0
        i=0
        while i < len(nums):
            if nums[i] == val:
                del nums[i]
            else:
                a=a+1
                i=i+1
        return a
        
