# 3146. Permutation Difference between Two Strings
# https://leetcode.com/problems/permutation-difference-between-two-strings/description/

class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        total=0
        for i in range(len(s)):
            for j in range(len(t)):
                if s[i]==t[j]:
                    total=total + abs(i-j)
        return total
