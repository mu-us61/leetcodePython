# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box
# 1769 no


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        size=len(boxes)
        listem=list(map(int,boxes))
        out=[]
        for i in range(size):
            yol=0
            for j in range(size):
                
                if not i==j:
                    if listem[j]:
                        yol= yol + abs(j-i)
            out.append(yol)
        return out
