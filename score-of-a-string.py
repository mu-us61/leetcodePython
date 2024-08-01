# https://leetcode.com/problems/score-of-a-string/

class Solution:
    def scoreOfString(self, s: str) -> int:
        sums=0
        list_of_asci = [ord(char) for char in s]

        for a in range(len(list_of_asci)-1):
            sums= sums + abs(list_of_asci[a] - list_of_asci[a+1])
        return sums
