#Link: https://leetcode.com/problems/merge-two-binary-trees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(p,q):
            if p==None and q==None:
                return None
            if p==None:
                return q
            if q==None:
                return p
            if p and q:
                root=TreeNode(p.val+q.val)
            root.left=dfs(p.left,q.left)
            root.right=dfs(p.right,q.right)
            return root
        
        return dfs(root1,root2)