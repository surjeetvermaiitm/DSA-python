#Link: https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        
        def f(n,memo={}):
            if n<0:
                return 0
            if n==0 or n==1:
                memo[n]=cost[n]
                return memo[n]
            if n not in memo:
                memo[n]=cost[n]+min(f(n-1),f(n-2))
                return memo[n]
            return memo[n]
        n=len(cost)
        return min(f(n-1),f(n-2))
            