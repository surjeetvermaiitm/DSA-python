#Link: https://leetcode.com/problems/frequency-of-the-most-frequent-element/

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # WRONG     
        # nums.sort(reverse=True)
        # n=len(nums)
        # ans=0
        # for i in range(1,len(nums)): 
        #     freq=1
        #     j=i
        #     while j<n and k>=0:
        #         diff=nums[i-1]-nums[j]
        #         k=k-diff
        #         j+=1
        #         if k>=0:
        #             freq+=1
        #     ans=max(ans,freq)
        # return ans
        #expand while num[r]*windowlen<total+k
        nums.sort()
        l,r=0,0
        res=0
        total=0
        while r<len(nums):
            total+=nums[r]
            while nums[r]*(r-l+1)>total+k:
                total-=nums[l]
                l+=1
            res=max(res,r-l+1)
            r+=1
        return res