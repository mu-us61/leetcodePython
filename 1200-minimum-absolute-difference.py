# https://leetcode.com/problems/minimum-absolute-difference
# 1200. Minimum Absolute Difference


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min=99999999999999
        result=[]
        for i in range(len(arr)):
            if i == len(arr)-1:
                break
            else:
                aday = arr[i+1] - arr[i]
                if aday < min:
                    min = aday
                    result.clear()
                    result.append([arr[i],arr[i+1]])
                elif aday == min:
                    result.append([arr[i],arr[i+1]])
        return result
        
