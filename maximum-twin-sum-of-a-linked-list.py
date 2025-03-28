# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/
# 2130

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        ll=[]
        while head:
            ll.append(head.val)
            head=head.next
        maxll=0
        for a,b in zip(ll,ll[::-1]):
            maxll=max(a+b,maxll)
        return maxll
