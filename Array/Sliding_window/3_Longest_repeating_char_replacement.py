#Link: https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        windowlen=0 #it is windowlen
        maxf=0
        freq={}
        for i in range(len(s)):
            freq[s[i]]=1+freq.get(s[i],0)
            maxf=max(maxf,freq[s[i]])
            if windowlen-maxf<k:
                windowlen+=1
            else:
                freq[s[i-windowlen]]-=1
        return windowlen
    
#Approach2
 def characterReplacement(self, s: str, k: int) -> int:
        count={}
        res=0
        l=0
        for r in range(len(s)):
            count[s[r]]=1+count.get(s[r],0)
            
            while (r-l+1)-max(count.values())>k:
                count[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
        return res
    
#Approch3
def characterReplacement(self, s: str, k: int) -> int:
    count={}
    res=0
    l=0
    maxf=0
    for r in range(len(s)):
        count[s[r]]=1+count.get(s[r],0)
        maxf=max(maxf,count[s[r]])
        while (r-l+1)-maxf>k:
            count[s[l]]-=1
            l+=1
        res=max(res,r-l+1)
    return res
    