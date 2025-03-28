# https://leetcode.com/problems/merge-in-between-linked-lists/
# 1669

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # Create a dummy node to handle edge cases easily
        dummy = ListNode(-1)
        dummy.next = list1
        
        # Pointers to traverse list1
        prev = dummy
        current = list1
        
        # Traverse to find the node just before the `a`-th node
        index = 0
        while current:
            if index == a:
                # Attach the start of list2 here
                prev.next = list2
                
                # Traverse to the end of list2
                while list2.next:
                    list2 = list2.next
                
                # Continue traversing list1 to find the node after the `b`-th node
                while current and index <= b:
                    current = current.next
                    index += 1
                
                # Connect the end of list2 to the node after the `b`-th node
                list2.next = current
                return dummy.next
            
            # Move to the next node in list1
            prev = prev.next
            current = current.next
            index += 1
        
        return dummy.next
