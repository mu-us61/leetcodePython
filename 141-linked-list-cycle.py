# https://leetcode.com/problems/linked-list-cycle
# 141

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current=head
        dummy=[]
        while current:
            dummy.append(current)
            if current.next in dummy:
                return True
            current=current.next
        return False
