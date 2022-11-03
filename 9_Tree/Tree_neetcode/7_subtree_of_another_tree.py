#Link: https://leetcode.com/problems/subtree-of-another-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
            if not subRoot:
                return True
            if not root:
                return False
            lans=self.isSubtree(root.left,subRoot)
            rans=self.isSubtree(root.right,subRoot)
            return lans or rans or self.isSameTree(root,subRoot)
        
    def isSameTree(self,p,q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        lans=self.isSameTree(p.left,q.left)
        rans=self.isSameTree(p.right,q.right)
        return lans and rans and p.val==q.val
        