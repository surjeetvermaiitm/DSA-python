#Link https://leetcode.com/problems/valid-palindrome-ii/

class Solution:
    def isPalindrome(self,st):
        l,h=0,len(st)-1
        while l<h:
            if st[l]!=st[h]:
                return False
            l+=1
            h-=1
        return True
    def validPalindrome(self, s: str) -> bool:
        l=0
        h=len(s)-1
        while l<h:
            if s[l]==s[h]:
                l+=1
                h-=1
                continue
            else:
                # print(s[l:h])
                # print(s[l+1:h+1])
                return self.isPalindrome(s[l:h]) or self.isPalindrome(s[l+1:h+1])
        return True
                
                