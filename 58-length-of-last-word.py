# 58
# https://leetcode.com/problems/length-of-last-word

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        count = 0
        i = -1
        # Fixing the condition
        if " " not in s:
            return len(s)
        while abs(i) <= len(s):
            if s[i] == " ":
                break
            count = count + 1
            i = i - 1
        return count
