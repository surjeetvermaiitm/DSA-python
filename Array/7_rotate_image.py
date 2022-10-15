#reverse each row and then take transpose
def solve(mat):
    # CODE HERE
    for row in mat:
        row.reverse()

    n=len(mat)
    for i in range(len(mat)):
        for j in range(n-i):
            mat[i][j],mat[n-1-j][n-1-i]=mat[n-1-j][n-1-i],mat[i][j]

    return mat