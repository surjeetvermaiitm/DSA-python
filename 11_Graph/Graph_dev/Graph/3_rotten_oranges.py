#Link: https://leetcode.com/problems/rotting-oranges/
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rotten_q = deque()
        m,n=len(grid),len(grid[0])
        fresh_oranges=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    fresh_oranges+=1
                elif grid[i][j]==2:
                    rotten_q.append((i,j,0))
        if fresh_oranges==0:
            return 0
        dir={(1,0),(-1,0),(0,1),(0,-1)}
        while rotten_q:
            ro_i,ro_j,t=rotten_q.popleft()
            for di,dj in dir:
                newo_i,newo_j=ro_i+di,ro_j+dj
                if -1<newo_i<m and -1<newo_j<n and grid[newo_i][newo_j]==1:
                    fresh_oranges-=1
                    if fresh_oranges==0:
                        return t+1
                    grid[newo_i][newo_j]=2
                    rotten_q.append((newo_i,newo_j,t+1))
        return -1