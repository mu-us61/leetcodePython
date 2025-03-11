# https://leetcode.com/problems/faulty-keyboard/description/
# 2810

class Solution:
    def finalString(self, s: str) -> str:
        result=[]
        for i in s:
            if i=="i":
                result=result[::-1]
            else:
                result.append(i)
        return "".join(map(str,result))
