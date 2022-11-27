#Link: https://leetcode.com/problems/house-robber-ii/

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        
        def f(n,num,memo):
            if n==0:
                memo[0]=num[0]
                return memo[0]
            if n==1:
                memo[1]=max(num[0],num[1])
                return memo[1]
            if n not in memo:
                memo[n]=max(num[n]+f(n-2,num,memo),f(n-1,num,memo))
                return memo[n]
            return memo[n]
        n=len(nums)
        l1=nums[1:]
        l2=nums[:-1]
        memo1={}
        memo2={}
        return max(f(n-2,l1,memo1),f(n-2,l2,memo2))
        
        