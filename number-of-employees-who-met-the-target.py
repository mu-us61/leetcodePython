# 2798. Number of Employees Who Met the Target
# https://leetcode.com/problems/number-of-employees-who-met-the-target/description/

class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        result=0
        for hour in hours:
            if hour >= target :
                result = result +1
        return result
