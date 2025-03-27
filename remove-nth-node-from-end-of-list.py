# https://leetcode.com/problems/remove-nth-node-from-end-of-list
# 19

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        count = 0
        while current:
            count += 1
            current = current.next

        index = count - n
        now = 0
        current = head
        if index==0:
            return head.next
        else:
            while current:
                if now == index - 1:
                    break
                now += 1
                current = current.next
        
            if current.next:
                current.next=current.next.next
            else:
                current.next=None
            return head
