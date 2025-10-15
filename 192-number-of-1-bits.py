# 191
# https://leetcode.com/problems/number-of-1-bits

class Solution:
    def hammingWeight(self, n: int) -> int:
        binary=bin(n)[2:]
        toStr=str(binary)
        return toStr.count("1")
