# https://leetcode.com/problems/sum-multiples/description/
# 2652. Sum Multiples


class Solution:
    def sumOfMultiples(self, n: int) -> int:
        targets=[]
        for num in range(1,n+1):
            if num%3==0 or num%5==0 or num%7==0 :
                targets.append(num)
        return sum(targets)
