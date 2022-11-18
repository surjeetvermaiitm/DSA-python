#Link: https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        ans=0
        visit=set()
        #DFS
        # def dfs(src):
        #     visit.add(src)
        #     for j in range(n):
        #         if isConnected[src][j]==1 and j not in visit:
        #             dfs(j)
        # for i in range(n):
        #     if i not in visit:
        #         ans+=1
        #         dfs(i)
        # return ans
        #BFS
        
        def bfs(src):
            visit.add(src)
            q=deque([src])
            while q:
                node=q.popleft()
                for j in range(n):
                    if isConnected[node][j]==1 and j not in visit:
                        visit.add(j)
                        q.append(j)
            
            
        for i in range(n):
            if i not in visit:
                ans+=1
                bfs(i)
        return ans
                