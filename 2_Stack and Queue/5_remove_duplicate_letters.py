#link: https://leetcode.com/problems/remove-duplicate-letters/

class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        m={}
        for i,ch in enumerate(s):
            m[ch]=i
        st=[]
        present=set()
        for i,e in enumerate(s):
            if e in present:
                continue
            while st and st[-1]>e and m[st[-1]]>i:
                t=st.pop()
                present.remove(t)
            st.append(e)
            present.add(e)
                
                
        return "".join(st)