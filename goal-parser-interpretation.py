# 1678. Goal Parser Interpretation
# https://leetcode.com/problems/goal-parser-interpretation/description/

class Solution:
    def interpret(self, command: str) -> str:
        result=""
        next=0
        for char in command:
            if char == "G":
                result += char
            elif char == "(":
                next=1
            elif char == "a":
                next=0
                result += "al"
            elif char == ")":
                if next == 1:
                    result += "o"
                    next =0 
        return result
