#Link: https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m1={e:s1.count(e) for e in s1}
        l=0
        r=len(s1)-1
        window=s2[l:r+1]
        m2={e:window.count(e) for e in window}
        while r<len(s2):
            b=True
            for k in m1:
                if m1[k]!=m2.get(k,0):
                    b=False
            if b==True:
                return True
            elif r-l+1<len(s1):
                return False
            else:
                m2[s2[l]]=m2[s2[l]]-1
                if r<len(s2)-1:
                    r+=1
                m2[s2[r]]=m2.get(s2[r],0)+1
                l+=1     
        return False
    
#Approach 2
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m1={e:s1.count(e) for e in s1}
        l=0
        r=len(s1)-1
        window=s2[l:r+1]
        m2={e:window.count(e) for e in window}
        while r<len(s2):
            # print(m1,m2)
            if m1==m2:
                return True
            elif r-l+1<len(s1):
                return False
            else:
                if m2[s2[l]]==1:
                    m2.pop(s2[l])
                else:
                    m2[s2[l]]=m2[s2[l]]-1
                        
                if r<len(s2)-1:
                    r+=1
                m2[s2[r]]=m2.get(s2[r],0)+1
                l+=1     
        return False
#T= O(26*n)
#S= O(26)

#Approach 3 --> T(O(n))
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        s1Count,s2Count=[0]*26,[0]*26
        for i in range(len(s1)):
            s1Count[ord(s1[i])-ord('a')]+=1
            s2Count[ord(s2[i])-ord('a')]+=1
        matches=0
        for i in range(26):
            matches+=(1 if s1Count[i]==s2Count[i] else 0)
        l=0
        for r in range(len(s1),len(s2)):
            if matches==26:
                return True
            index=ord(s2[r])-ord('a')
            s2Count[index]+=1
            if s1Count[index]==s2Count[index]:
                matches+=1
            elif s1Count[index]+1==s2Count[index]:
                matches-=1
                
            index=ord(s2[l])-ord('a')
            s2Count[index]-=1
            if s1Count[index]==s2Count[index]:
                matches+=1
            elif s1Count[index]-1==s2Count[index]:
                matches-=1
            l+=1
        return matches==26