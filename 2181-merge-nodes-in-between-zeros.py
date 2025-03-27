# https://leetcode.com/problems/merge-nodes-in-between-zeros
# 2181

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: Create a dummy node to build the result list
        dummy = ListNode(0)
        current = dummy
        
        # Step 2: Traverse the input list
        sums = 0
        head = head.next  # Skip the first zero (guaranteed to exist)
        
        while head:
            if head.val == 0:
                # When we encounter a zero, create a new node with the accumulated sum
                current.next = ListNode(sums)
                current = current.next
                sums = 0  # Reset the sum for the next segment
            else:
                # Accumulate the values of nodes between zeros
                sums += head.val
            
            # Move to the next node
            head = head.next
        
        # Step 3: Return the merged list (skip the dummy node)
        return dummy.next 
