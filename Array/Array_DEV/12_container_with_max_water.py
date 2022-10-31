# use two pointer

def solve(n, arr):
    # CODE HERE
    l=0
    r=n-1
    ans=0
    while(l<=r):
        ans=max(ans,min(arr[l],arr[r])*(r-l))
        if(arr[l]<arr[r]):
            l+=1
        else:
            r-=1
    return ans
