#Link: https://practice.geeksforgeeks.org/problems/bfs-traversal-of-graph/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=bfs_of_graph

import collections
class Solution:
    
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V, adj):
        # # code here
        ans=[]
        visit=set([0])
        q=collections.deque([0])
        while q:
            node=q.popleft()
            ans.append(node)
            for nbr in adj[node]:
                if nbr not in visit:
                    visit.add(nbr)
                    q.append(nbr)
        return ans
    
#DFS
#User function Template for python3
import collections

class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        # code here
        ans=[]
        visit=set()
        def dfs(src):
            visit.add(src)
            ans.append(src)
            for nbr in adj[src]:
                if nbr not in visit:
                    dfs(nbr)
        for i in range(V):
            if i not in visit:
                dfs(i)
            
        return ans
