# https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/
# 2894. Divisible and Non-divisible Sums Difference


class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1=num2=0
        for i in range(1,n+1):
            if i%m==0:
                num2 = num2 + i
            else:
                num1 = num1 +i
        return num1-num2 
        
