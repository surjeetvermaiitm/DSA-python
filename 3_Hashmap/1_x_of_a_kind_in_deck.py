# Link: https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/

class Solution(object):
    def gcd(self,a,b):
        if b==0:
            return a
        else:
            return self.gcd(b,a%b)
        
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        if len(deck)==1:
            return False
        d={}
        for x in deck:
            d[x]=1+d.get(x,0)
            
        gcd_ans=d[deck[0]]

        for val in d.values():
            gcd_ans=self.gcd(gcd_ans,val)
            
        return gcd_ans>1