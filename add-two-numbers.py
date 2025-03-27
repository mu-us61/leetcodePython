# https://leetcode.com/problems/add-two-numbers
# 2

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        current = dummy_head
        extra = 0
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            sums = val1 + val2 + extra
            extra = sums // 10
            singledigit = sums % 10
            current.next = ListNode(singledigit)
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if extra:
            current.next = ListNode(extra)
        return dummy_head.next
