#Link: https://leetcode.com/problems/clone-graph/

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node==None:
            return None
        oldToNew={}
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            copy=Node(node.val)
            oldToNew[node]=copy
            for nbr in node.neighbors:
                copy.neighbors.append(dfs(nbr))
            return copy
        return dfs(node)