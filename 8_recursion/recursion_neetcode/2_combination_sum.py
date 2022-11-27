#Leetcode: https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         res=[]
        
#         cur=[]
#         def dfs(i,total):
#             if total==target:
#                 res.append(cur.copy())
#                 return
#             if i>=len(candidates) or total>target:
#                 return
#             cur.append(candidates[i])
#             dfs(i,total+candidates[i])
#             cur.pop()
#             dfs(i+1,total)
#         dfs(0,0)
#         return res
#or
    
        res=[]
        
        def dfs(i,total,cur):
            if total==target:
                res.append(cur.copy())
                return
            if i>=len(candidates) or total>target:
                return
            cur.append(candidates[i])
            dfs(i,total+candidates[i],cur)
            cur.pop()
            dfs(i+1,total,cur)
        dfs(0,0,[])
        return res