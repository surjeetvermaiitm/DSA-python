#link: https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        def f(n,memo={}):
            if n==0:
                memo[0]=nums[0]
                return memo[0]
            if n==1:
                memo[1]=max(nums[0],nums[1])
                return memo[1]
            if n not in memo:
                memo[n]=max(nums[n]+f(n-2),f(n-1))
                return memo[n]
            return memo[n]
        return f(n-1)