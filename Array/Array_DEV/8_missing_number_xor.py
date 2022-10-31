from operator import xor


def solve(n, arr):
    # CODE HERE
    sum_req=int(n*(n+1)/2)
    return sum_req-sum(arr)

#method 2
# using xor
def solve(n, arr):
    # CODE HERE
    x=0
    for i in range(n+1):
        x=x^i

    for num in arr:
        x=x^num
    return x