def promising(i, n, col):
    for k in range(1, i):
        if col[i] == col[k] or abs(col[i] - col[k]) == abs(i - k):
            return False
    return True

def nqueens(i, n, col):
    if i == n:
        print("found=", col[1:])
    else:
        for c in range(1, n + 1):
            col[i+1] = c
            if promising(i+1, n, col):
                nqueens(i+1, n, col)


# Example 1
print("######Example 1######")
n = 4
col = [0] * (n + 1)
nqueens(0, n, col)

# Example 2 - Your Custom Case
print("######Example 2 #######") 
n = 5  
col = [0] * (n + 1)
nqueens(0, n, col)