# https://leetcode.com/problems/longest-common-prefix
# 14. Longest Common Prefix




class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        min_word = min(strs,key=len)

        for indx,letter in enumerate(min_word):
            for other in strs:
                if other[indx] != letter:
                    return min_word[:indx]
        return min_word
