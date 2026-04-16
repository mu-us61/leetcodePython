# https://leetcode.com/problems/range-sum-query-immutable/
# 303. Range Sum Query - Immutable


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right+1])
        
