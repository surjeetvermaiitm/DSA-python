#Link: https://leetcode.com/problems/sum-of-left-leaves/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        q=deque([root])
        ans=0
        while q:
            node=q.popleft()
            if node.left:
                q.append(node.left)
                if not node.left.left and not node.left.right:
                    ans+=node.left.val
            if node.right:
                q.append(node.right)
        return ans
        