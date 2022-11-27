#Link: https://leetcode.com/problems/permutations-ii/

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        perm=[]
        
        count={n:0 for n in nums}
        for n in nums:
            count[n]+=1
        def dfs():
            if len(perm)==len(nums):
                res.append(perm[:])
                return
            for n in count:
                if count[n]>0:
                    perm.append(n)
                    count[n]-=1
                    dfs()
                    perm.pop()
                    count[n]+=1
        dfs()
        return res