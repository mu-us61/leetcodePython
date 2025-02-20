# https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/
# 3300

class Solution:
    def minElement(self, nums: List[int]) -> int:
        newnums=[]
        for i in nums:
            sum=0
            for j in str(i):
                sum=sum+int(j)
            newnums.append(sum) # what if the number is 0 ?
        return min(newnums)
