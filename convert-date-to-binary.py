
# https://leetcode.com/problems/convert-date-to-binary/description/
# 3280. Convert Date to Binary

class Solution:
    def convertDateToBinary(self, date: str) -> str:
        # binary_string = bin(num)[2:]  # '101010'
        yyyy=int(date[0:4])
        mm=int(date[5:7])
        dd=int(date[-2:])
        yyyy=bin(yyyy)[2:]
        mm=bin(mm)[2:]
        dd=bin(dd)[2:]
        return yyyy + "-" + mm + "-" + dd
