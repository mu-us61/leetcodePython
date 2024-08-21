# https://leetcode.com/problems/minimum-number-game/description/
# 2974. Minimum Number Game



class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        sortedlist = sorted(nums)
        for i in range(0,len(nums),2):
            sortedlist[i] , sortedlist[i+1] = sortedlist[i+1] , sortedlist[i]
        return sortedlist
