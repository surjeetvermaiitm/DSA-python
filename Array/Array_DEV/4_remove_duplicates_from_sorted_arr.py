def solve(n, arr):
    # CODE HERE
    ans=[arr[0]]
    for el in arr:
        if el!=ans[-1]:
            ans.append(el)

    return ans