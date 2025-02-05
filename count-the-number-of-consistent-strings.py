# https://leetcode.com/problems/count-the-number-of-consistent-strings/description/
# 1684. Count the Number of Consistent Strings


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        count=0
        for word in words:
            is_okay=True
            for letter in word:
                if letter in allowed:
                    pass
                else:
                    is_okay=False
            if is_okay == True:
                    count=count+1    
        return count
