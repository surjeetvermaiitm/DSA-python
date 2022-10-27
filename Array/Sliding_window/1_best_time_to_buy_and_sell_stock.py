#Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==0 or len(prices)==1:
            return 0
            
        min_so_far=prices[0]
        ans=0
        for i in range(1,len(prices)):
            ans=max(ans,prices[i]-min_so_far)
            min_so_far=min(min_so_far,prices[i])
        return ans
#using two pointer
class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         if len(prices)==0 or len(prices)==1:
#             return 0
            
#         min_so_far=prices[0]
#         ans=0
#         for i in range(1,len(prices)):
#             ans=max(ans,prices[i]-min_so_far)
#             min_so_far=min(min_so_far,prices[i])
#         return ans
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        maxP=0
        while r<len(prices):
            if prices[l]<prices[r]:
                profit=prices[r]-prices[l]
                maxP=max(maxP,profit)
            else:
                l=r
            r+=1
        return maxP