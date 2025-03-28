# https://leetcode.com/problems/intersection-of-two-linked-lists
# 160

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
 # Step 1: Calculate lengths of both lists
        lenA, lenB = 0, 0
        currentA, currentB = headA, headB
        
        while currentA:
            lenA += 1
            currentA = currentA.next
        
        while currentB:
            lenB += 1
            currentB = currentB.next
        
        # Step 2: Align starting points by skipping nodes in the longer list
        currentA, currentB = headA, headB
        if lenA > lenB:
            for _ in range(lenA - lenB):
                currentA = currentA.next
        elif lenB > lenA:
            for _ in range(lenB - lenA):
                currentB = currentB.next
        
        # Step 3: Traverse both lists to find the intersection
        while currentA and currentB:
            if currentA == currentB:
                return currentA  # Intersection found
            currentA = currentA.next
            currentB = currentB.next
        
        # Step 4: No intersection found
        return None
