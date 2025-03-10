# https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone
# 2037

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        total_moves=0
        for seat,student in zip(seats,students):
            total_moves += abs(seat-student)
        
        return total_moves
