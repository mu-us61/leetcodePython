# https://leetcode.com/problems/split-a-string-in-balanced-strings
# 1221. Split a String in Balanced Strings


class Solution:
    @staticmethod
    def is_equal(s):
        R=0
        L=0
        for char in s:
            if char == "R":
                R=R+1
            elif char == "L":
                L=L+1
        return R == L

    def balancedStringSplit(self, s: str) -> int:
        output_count=0
        temp=[]
        size=len(s)
        for i in range(size):
            if self.is_equal(s[0:i+1]) and self.is_equal(s[i+1:]):
                output_count += 1

        return output_count
        
