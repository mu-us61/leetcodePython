# https://leetcode.com/problems/merge-two-sorted-lists
# 21

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyhead = ListNode(0)
        current = dummyhead
        while True:
            if not list1 or not list2:
                break 
            if list1.val <= list2.val:
                current.next = ListNode(list1.val)
                current = current.next
                list1 = list1.next
               
            else:
                current.next=ListNode(list2.val)
                current = current.next
                list2 = list2.next
              
        if not list2:
            current.next = list1
        if not list1:
            current.next = list2
        return dummyhead.next
