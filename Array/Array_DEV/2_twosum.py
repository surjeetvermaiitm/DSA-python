def solve(n, nums, target):
    # CODE HERE
    myset=dict()
    for i,n in enumerate(nums):
        diff=target-n
        if diff in myset:
            return [myset[diff],i]
        myset[n]=i