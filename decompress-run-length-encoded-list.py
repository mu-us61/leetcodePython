# https://leetcode.com/problems/decompress-run-length-encoded-list/description/
# 1313. Decompress Run-Length Encoded List

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result=[]
        for i in range(len(nums)//2):
            for j in range(nums[2*i]):
                result.append(nums[2*i+1])
        return result
