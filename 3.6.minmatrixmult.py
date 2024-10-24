def minimum(i, j, M, d):
    minvalue, mink = INF, 0
    for k in range(i, j):
        # Calculate the cost of multiplying matrices from i to k, and from k+1 to j, 
        # and then multiplying the resulting matrices together.
        cost = M[i][k] + M[k + 1][j] + d[i - 1] * d[k] * d[j]
        if cost < minvalue:
            minvalue = cost
            mink = k
    return minvalue, mink


def minmult(n, d):
    M = [[INF] * (n + 1) for _ in range(n + 1)]
    P = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        M[i][i] = 0  # Zero cost for multiplying one matrix
    
    for diagonal in range(1, n):
        for i in range(1, n - diagonal + 1):
            j = i + diagonal
            M[i][j], P[i][j] = minimum(i, j, M, d)
    
    return M[1][n], M, P
    
def order(i, j, P):
    if i == j:
        return "A" + str(i)
    else:
        k = P[i][j]
        left_order = order(i, k, P)
        right_order = order(k + 1, j, P)
        return "(" + left_order + right_order + ")"

INF = float("inf")

# Example 1
print("######Example 1######")
n = 6
d = [5, 2, 3, 4, 6, 7, 8]
minvalue, M, P = minmult(n, d)
print("M = ")
for i in range(1, n + 1):
    print(M[i][i:])
print("P = ")
for i in range(1, n + 1):
    print(P[i][i:])
print("minmult = ", minvalue)

multorder = order(1, n, P)
print(multorder)


# # Example 2 - Your Custom Case
# print("######Example 2 #######") 
# # Insert your example here
n = 6
d = [1, 8, 3, 9, 7, 10, 2]
minvalue, M, P = minmult(n, d)
print("M = ")
for i in range(1, n + 1):
    print(M[i][i:])
print("P = ")
for i in range(1, n + 1):
    print(P[i][i:])
print("minmult = ", minvalue)

multorder = order(1, n, P)
print(multorder)