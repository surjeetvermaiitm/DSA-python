#Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

#approach1
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sindices=[-1]*256
        start=-1
        ans=0
        for i in range(len(s)):
            if sindices[ord(s[i])]>start:
                start=sindices[ord(s[i])]
            sindices[ord(s[i])]=i
            ans=max(ans,i-start)
        return ans
#approach2
class Solution:
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     sindices=[-1]*256
    #     start=-1
    #     ans=0
    #     for i in range(len(s)):
    #         if sindices[ord(s[i])]>start:
    #             start=sindices[ord(s[i])]
    #         sindices[ord(s[i])]=i
    #         ans=max(ans,i-start)
    #     return ans
    #sliding window
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet=set()
        l=0
        ans=0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            ans=max(ans,r-l+1)
        return ans
                