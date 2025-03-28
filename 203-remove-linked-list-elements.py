# https://leetcode.com/problems/remove-linked-list-elements
# 203

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = None

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Step 1: Handle cases where the head itself needs to be removed
        while head and head.val == val:
            head = head.next
        
        # Step 2: Traverse the rest of the list to remove nodes with value `val`
        current = head
        prev = None
        
        while current:
            if current.val == val:
                # Remove the current node by updating the previous node's `next` pointer
                if prev:
                    prev.next = current.next
            else:
                # Update `prev` only if the current node is not removed
                prev = current
            # Move to the next node
            current = current.next
        
        return head
