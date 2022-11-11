#Link:https://leetcode.com/problems/valid-parentheses/
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        myset={'{':-1,'}':1,'(':-2,')':2,'[':-3,']':3}
        stack=[]
        for ele in s:
            if myset[ele]<0:
                stack.append(ele)
            else:
                if len(stack)==0:
                    return False
                else:
                    if myset[stack.pop()]+myset[ele]!=0:
                        return False
        return len(stack)==0
        # ct=0
        # stack=[]
        # for brace in s:
        #     if myset[brace] is -1 or myset[brace] is -2 or myset[brace] is -3:
        #         stack.append(myset[brace])
        #         ct+=myset[brace]
        #     else:
        #         if len(stack)!=0:
        #             end=stack.pop()
        #             if end+myset[brace]!=0:
        #                 return False
        #             else:
        #                 ct+=myset[brace]
        #         else:
        #             return False
        # return ct==0
        
        