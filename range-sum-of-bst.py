# https://leetcode.com/problems/range-sum-of-bst/
# 938

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return 0


        sum=0
        if  low <= root.val <= high:
            sum += root.val
        
        leftsum= self.rangeSumBST(root.left,low,high)
        rightsum= self.rangeSumBST(root.right,low,high)
        return sum+leftsum+rightsum
