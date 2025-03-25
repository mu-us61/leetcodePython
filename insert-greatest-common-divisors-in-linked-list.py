# https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list
# 2807

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def greatest_common(self,num1,num2):
        minValue=min(num1,num2)
        divisor=1
        for i in range(1,minValue+1):
            if num1%i==0 and num2%i==0:
                divisor=i
        return divisor

    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current=head
        while current and current.next:
            gc=self.greatest_common(current.val,current.next.val)
            newnode=ListNode(gc)

            nextnode= current.next

            newnode.next=nextnode
            current.next=newnode
            
            current=nextnode
        return head
