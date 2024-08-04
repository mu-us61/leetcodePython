# 2942. Find Words Containing Character
# https://leetcode.com/problems/find-words-containing-character/description/

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result=[]
        for wordindex in range(len(words)):
            if x in words[wordindex]:
                result.append(wordindex)

        return result
