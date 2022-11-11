#Link: https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue(object):

    def __init__(self):
        self.st1=[]
        self.st2=[]
    
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.st1.append(x)
        
        

    def pop(self):
        """
        :rtype: int
        """
        if not self.st2:
            while self.st1:
                self.st2.append(self.st1.pop())
        return self.st2.pop()
                

    def peek(self):
        """
        :rtype: int
        """
        if not self.st2:
            while self.st1:
                self.st2.append(self.st1.pop())
        return self.st2[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return (len(self.st1)==0 and len(self.st2)==0)
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()



# method 2
class MyQueue(object):

    def __init__(self):
        self.st1=[]
        self.st2=[]
    
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        
        while self.st2:
            self.st1.append(self.st2.pop())
        self.st2.append(x)

        while self.st1:
            self.st2.append(self.st1.pop())    

    def pop(self):
        """
        :rtype: int
        """
        
        return self.st2.pop()
                

    def peek(self):
        """
        :rtype: int
        """
        
        return self.st2[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return (len(self.st1)==0 and len(self.st2)==0)
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()