# https://leetcode.com/problems/find-if-digit-game-can-be-won/
# 3232. Find if Digit Game Can Be Won


class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        tek_basamak=[]
        cift_basamak=[]
        for sayi in nums:
            if len(str(sayi)) == 1:
                tek_basamak.append(sayi)
            elif len(str(sayi)) == 2:
                cift_basamak.append(sayi)
        result = True
        return result if not sum(tek_basamak) == sum(cift_basamak) else False
