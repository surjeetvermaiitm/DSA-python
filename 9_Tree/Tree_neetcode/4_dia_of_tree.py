#Link: https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:  
        def diameter_helper(root):
            if root==None:
                return [0,0]
            ld,lh=diameter_helper(root.left)
            rd,rh=diameter_helper(root.right)
            curr_dia=lh+rh
            h=max(lh,rh)+1
            return [max(curr_dia,max(ld,rd)),h]
        
        return diameter_helper(root)[0]  

        
    # def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:  
    #     ans=[0]
    #     def dfs(root):
    #         if root==None:
    #             return 0
    #         lh=dfs(root.left)
    #         rh=dfs(root.right)
    #         ans[0]=max(ans[0],lh+rh)
    #         return max(lh,rh)+1
    #     dfs(root)
    #     return ans[0]
    
        