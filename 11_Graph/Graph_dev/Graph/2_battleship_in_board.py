#Link: https://leetcode.com/problems/battleships-in-a-board/

class Solution(object):

        
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        ans=0
        m,n=len(board),len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j]=='X' and (i==0 or board[i-1][j]!='X') and (j==0 or board[i][j-1]!='X'):
                    ans+=1
        return ans
                    