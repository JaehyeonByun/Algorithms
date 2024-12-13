def promising(i, n, col):
    is_promising = True
    k = 1
    while k < i and is_promising:
        if col[i] == col[k] or abs(col[i] - col[k]) == (i - k):
            is_promising = False
        k += 1
    return is_promising

def nqueens(i, n, col):
    if promising(i, n, col):
        if i == n:
            print("found=", col[1:])
        else:
            for j in range(1, n+1):
                col[i+1] = j
                nqueens(i+1, n, col)

# Example 1
print("######Example 1######")
n = 4
col = [0] * (n + 1)
nqueens(0, n, col)

# Example 2 - Your Custom Case
print("######Example 2 #######")
# Let's try with n = 5
n = 5
col = [0] * (n + 1)
nqueens(0, n, col)
