# 28. Find the Index of the First Occurrence in a String

# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        j = 0
        start_index = 0

        while i < len(haystack):
            if haystack[i] == needle[j]:
                if j == 0:  # mark where match starts
                    start_index = i
                j += 1

                if j == len(needle):  # full match
                    return start_index
                i += 1
            else:
                if j > 0:
                    # restart search from next after start_index
                    i = start_index + 1
                else:
                    i += 1
                j = 0

        return -1
