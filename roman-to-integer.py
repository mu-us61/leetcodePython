# https://leetcode.com/problems/roman-to-integer/
# 13. Roman to Integer

class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
        }
        num = 0
        prev_value = 0
        
        for char in s[::-1]:  # Reverse the string to handle subtraction cases more easily
            value = values[char]
            if value < prev_value:
                num -= value
            else:
                num += value
            prev_value = value

        return num
