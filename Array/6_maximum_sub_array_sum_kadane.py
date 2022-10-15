def solve(n, arr):
    # CODE HERE
    max_so_far=arr[0]
    ans=arr[0]

    for i in range(1,len(arr)):
        max_so_far=max(arr[i],max_so_far+arr[i])
        ans=max(ans,max_so_far)
    return ans

#method 2
def solve(n, arr):
    # CODE HERE
    max_so_far=0
    ans=-1e9

    for i in range(0,len(arr)):
        max_so_far+=arr[i]
        if ans<max_so_far:
            ans=max_so_far
        if max_so_far<0:
            max_so_far=0
    return ans