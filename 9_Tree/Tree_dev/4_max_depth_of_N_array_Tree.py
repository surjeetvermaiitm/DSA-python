#Link: https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root==None:
            return 0
        q=deque([root])
        level=0
        while q:
            n=len(q)
            level+=1
            for i in range(n):
                node=q.popleft()
                for j in node.children:
                    q.append(j)
        return level
                    
                    
        
            
        