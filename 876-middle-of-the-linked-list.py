# https://leetcode.com/problems/middle-of-the-linked-list/
# 876

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lenght=0
        start=head
        while head:
            lenght += 1
            head=head.next
        chosen= lenght//2 + 1
        index = chosen -1

        head=start
        count=0
        while head:
            if index == count:
                return head
            else:
                count += 1
                head=head.next
            
