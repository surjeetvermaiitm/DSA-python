#Link: https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [0,True]
            lh,lb=dfs(root.left)
            rh,rb=dfs(root.right)
            h=max(lh,rh)+1
            b=lb and rb and abs(rh-lh)<=1
            return [h,b]
        return dfs(root)[1]