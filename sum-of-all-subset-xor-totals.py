# https://leetcode.com/problems/sum-of-all-subset-xor-totals/
# 1863. Sum of All Subset XOR Totals

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0
        
        # Loop over all possible subset lengths: from 0 (empty) to len(nums)
        for r in range(len(nums) + 1):
            # Generate all subsets (combinations) of length r
            for subset in itertools.combinations(nums, r):
                xor_value = 0
                # Compute XOR of all elements in the current subset
                for num in subset:
                    xor_value ^= num
                # Add the XOR total of this subset to the overall total
                total += xor_value
        
        return total
