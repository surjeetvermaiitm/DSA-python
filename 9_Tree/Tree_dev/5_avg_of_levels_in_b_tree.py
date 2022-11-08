#Link: https://leetcode.com/problems/average-of-levels-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root==None:
            return []
        q=deque([root])
        ans=[]
        while q:
            n=len(q)
            sum=0
            for i in range(n):
                node=q.popleft()
                sum+=node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(sum/n)
        return ans
        