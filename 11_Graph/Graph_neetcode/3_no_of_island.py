#Link: https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows,cols=len(grid),len(grid[0])
        visit=set()
        island=0
        # def bfs(r,c):
        #     q=collections.deque()
        #     visit.add((r,c))
        #     q.append((r,c))
        #     while q:
        #         row,col=q.popleft()
        #         #q.pop()-->DFS iterative
        #         dir=[[1,0],[-1,0],[0,1],[0,-1]]
        #         for dr,dc in dir:
        #             nr,nc=row+dr,col+dc
        #             if ((nr) in range(rows) and (nc) in range(cols) and grid[nr][nc]=="1" and (nr,nc) not in visit):
        #                 q.append((nr,nc))
        #                 visit.add((nr,nc))
        dir=[[1,0],[-1,0],[0,1],[0,-1]]
        def dfs(r,c):
            visit.add((r,c))
            for dr,dc in dir:
                nr=r+dr
                nc=c+dc
                if ((nr) in range(rows) and (nc) in range(cols) and grid[nr][nc]=="1" and (nr,nc) not in visit):
                    dfs(nr,nc)
                                 
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visit:
                    dfs(r,c)
                    island+=1
        return island