# https://leetcode.com/problems/check-balanced-string/description/
# 3340

class Solution:
    def isBalanced(self, num: str) -> bool:
        result=0
        swtch=-1
        for i in num:
            result+= int(i)*swtch
            swtch= swtch * -1
        return result==0
