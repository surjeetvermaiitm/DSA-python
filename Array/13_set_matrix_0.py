#vvi
def solve(matrix):
    # CODE HERE
    m,n=len(matrix),len(matrix[0])
    r,c=False,False

    for j in range(n):
        if matrix[0][j]==0:
            r=True
            break
    for i in range(m):
        if matrix[i][0]==0:
            c=True
            break
    for i in range(m):
        for j in range(n):
            if matrix[i][j]==0:
                matrix[i][0]=0
                matrix[0][j]=0
    for i in range(1,m):
        if matrix[i][0]==0:
            for j in range(1,n):
                matrix[i][j]=0
    for j in range(1,n):
        if matrix[0][j]==0:
            for i in range(1,m):
                matrix[i][j]=0
    if c:
        for i in range(m):
            matrix[i][0]=0
    if r:
        for j in range(n):
            matrix[0][j]=0

    return matrix