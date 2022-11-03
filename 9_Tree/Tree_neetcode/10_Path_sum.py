#Link : https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        curSum=0
        def dfs(node,curSum):
            if not node:
                return False
            curSum+=node.val
            #leaf node
            if not node.left and not node.right :
                return curSum==targetSum
            return dfs(node.left,curSum) or dfs(node.right,curSum)
        
        return dfs(root,0)