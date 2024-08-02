#https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        result=0
        for i in nums:
            if i%3 == 0:
                pass
            else:
                result= result +1
        return result
