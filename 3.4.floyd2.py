def floyd2(n, W):
    P = [[-1] * (n) for _ in range(n)]
    D = [row[:] for row in W]  # Create a copy of W to avoid modifying the original matrix

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if D[i][k] + D[k][j] < D[i][j]:
                    D[i][j] = D[i][k] + D[k][j]
                    P[i][j] = k

    return D, P

def path(i, j):
    k = P[i][j]
    if k != -1:
        path(i, k)
        print("v" + str(k), end = " ")
        path(k, j)
    
INF = float("inf")

# Example 1
print("######Example 1######")
n = 5
W = [[0,    1,      INF,    1,      5],     # v0 -> vi
     [9,    0,      3,      2,      INF],   # v1 -> vi
     [INF,  INF,    0,      4,      INF],   # v2 -> vi
     [INF,  INF,    2,      0,      3],     # v3 -> vi
     [3,    INF,    INF,    INF,    0]]     # v4 -> vi
  
D, P = floyd2(n, W)
print("D = ")
for i in range(n):
    print(D[i])
print("P = ")
for i in range(n):
    print(P[i])

path(4, 2)

# # Example 2 - Your Custom Case
# print("######Example 2 #######") 
# # Insert your example here
n = 4
W = [[0,    5,      INF,    10],  # v0 -> vi
     [INF,  0,      3,      INF],  # v1 -> vi
     [INF,  INF,    0,      1],    # v2 -> vi
     [INF,  INF,    INF,    0]]    # v3 -> vi

D, P = floyd2(n, W)
print("D = ")
for i in range(n):
    print(D[i])
print("P = ")
for i in range(n):
    print(P[i])

path(0,3)