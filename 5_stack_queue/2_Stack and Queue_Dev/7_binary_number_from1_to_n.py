import collections

q = collections.deque() 

q.append("1")
n=10
while n:
    n-=1
    s1=q.popleft()
    print(s1)
    
    s2=s1
    q.append(s1+"0")
    q.append(s2+"1")
    
    

