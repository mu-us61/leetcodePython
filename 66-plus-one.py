# 66
# https://leetcode.com/problems/plus-one

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Step 1: convert digits list to integer manually
        num = 0
        for d in digits:
            num = num * 10 + d

        # Step 2: add one
        num = num + 1

        # Step 3: convert integer back to list of digits manually
        result = []
        for ch in str(num):
            result.append(int(ch))

        return result
