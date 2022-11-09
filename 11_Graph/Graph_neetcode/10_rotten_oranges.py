#Link: https://leetcode.com/problems/rotting-oranges/

class Solution:
    # def orangesRotting(self, grid: List[List[int]]) -> int:
    #     rotten_q = deque()
    #     m,n=len(grid),len(grid[0])
    #     fresh_oranges=0
    #     for i in range(m):
    #         for j in range(n):
    #             if grid[i][j]==1:
    #                 fresh_oranges+=1
    #             elif grid[i][j]==2:
    #                 rotten_q.append((i,j,0))
    #     if fresh_oranges==0:
    #         return 0
    #     dir={(1,0),(-1,0),(0,1),(0,-1)}
    #     while rotten_q:
    #         ro_i,ro_j,t=rotten_q.popleft()
    #         for di,dj in dir:
    #             newo_i,newo_j=ro_i+di,ro_j+dj
    #             if -1<newo_i<m and -1<newo_j<n and grid[newo_i][newo_j]==1:
    #                 fresh_oranges-=1
    #                 if fresh_oranges==0:
    #                     return t+1
    #                 grid[newo_i][newo_j]=2
    #                 rotten_q.append((newo_i,newo_j,t+1))
    #     return -1
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        
        q=deque()
        time,fresh=0,0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    fresh+=1
                elif grid[r][c]==2:
                    q.append([r,c])
        dir=[[0,1],[0,-1],[1,0],[-1,0]]
        while q and fresh>0:     
            for i in range(len(q)):
                r,c=q.popleft()
                for dr,dc in dir:
                    row,col=r+dr,c+dc
                    #if in bounds and fresh, make rotten
                    if (row<0 or row==rows or col<0 or col==cols or grid[row][col]!=1):
                        continue
                    grid[row][col]=2
                    q.append([row,col])
                    fresh-=1
            time+=1
        return time if fresh==0 else -1
    
    