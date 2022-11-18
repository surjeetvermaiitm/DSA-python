#Link: https://practice.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=dfs_of_graph

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