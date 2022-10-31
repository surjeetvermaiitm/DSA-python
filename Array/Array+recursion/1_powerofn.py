def solve(x, n):
    # CODE HERE
    if n==0:
        return 1
    if (n==1):
        return x
    if(n<0):
        x=1/x
        n=-1*n
    p=solve(x,n//2)

    if(n%2==0):
        return p*p
    else:
        return p*p*x