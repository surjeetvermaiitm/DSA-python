def solve(s1, s2):
    # CODE HERE
    if(len(s1)!=len(s2)):
        return 0
    m={}
    for i in range(len(s1)):
        m[s1[i]]=1+m.get(s1[i],0)
        m[s2[i]]=m.get(s2[i],0)-1

    for k in m.values():
        if k!=0:
            return 0
    return 1
    