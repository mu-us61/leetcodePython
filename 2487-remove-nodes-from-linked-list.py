# https://leetcode.com/problems/remove-nodes-from-linked-list/
# 2487

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        mylist = []
        
        # Step 1: Populate `mylist` with all node values
        while current:
            mylist.append(current.val)
            current = current.next
        
        # Step 2: Precompute `max_from_right` array
        # This stores the maximum value from each index to the end of the list
        max_from_right = [0] * len(mylist)  # Initialize array
        max_from_right[-1] = mylist[-1]  # Last element is the max for itself
        for i in range(len(mylist) - 2, -1, -1):  # Traverse backwards
            max_from_right[i] = max(mylist[i], max_from_right[i + 1])
        
        # Step 3: Traverse the linked list again and remove nodes
        current = head
        prev = None
        index = 0
        
        while current:
            # Compare current node's value with `max_from_right[index]`
            if current.val < max_from_right[index]:
                if prev is None:
                    # If `prev` is None, it means we are removing the head
                    head = current.next  # Update head to the next node
                else:
                    # Otherwise, skip the current node by updating `prev.next`
                    prev.next = current.next
            else:
                # Move `prev` to the current node only if it's not removed
                prev = current
            
            # Move to the next node and increment the index
            current = current.next
            index += 1
        
        # Step 4: Return the modified head
        return head
