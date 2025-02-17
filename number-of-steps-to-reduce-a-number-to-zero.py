# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
# 1342

class Solution:
    def numberOfSteps(self, num: int) -> int:
        n=0
        while(num>0):
            if num % 2 == 0:
                num=num//2
                n+=1
            else:
                num-=1
                n+=1
        return n
            
