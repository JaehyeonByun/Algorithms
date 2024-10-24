def prim(n, W):
    F = []
    for i in range(2, n + 1):
        nearest[i] = 1
        distance[i] = W[1][i]
    
    for _ in range(n - 1):
        min_dist = INF
        vnear = -1
 
        for i in range(2, n + 1):
            if 0 <= distance[i] < min_dist:
                min_dist = distance[i]
                vnear = i
        F.append((nearest[vnear], vnear, W[nearest[vnear]][vnear]))
     
        distance[vnear] = -1

        for i in range(2, n + 1):
            if W[vnear][i] < distance[i]:
                distance[i] = W[vnear][i]
                nearest[i] = vnear
    
    return F
                
INF = float("inf")

# Example 1
print("######Example 1######")
n = 5 # the number of vertices
W = [ # adjacency matrix
        [INF,    INF,    INF,    INF,    INF,     INF],
        [INF,      0,      1,      3,    INF,     INF], 
        [INF,      1,      0,      3,      6,     INF],
        [INF,      3,      3,      0,      4,       2],
        [INF,    INF,      6,      4,      0,       5],
        [INF,    INF,    INF,      2,      5,       0]
    ]
nearest = [-1] * (n + 1)
distance = [-1] * (n + 1)

F = prim(n, W)
for edge in F:
    print(edge)

# Example 2 - Custom Case
print("######Example 2 #######")
n = 4
W = [
    [INF, INF, INF, INF, INF],
    [INF, 0,    2,    INF, 6],
    [INF, 2,    0,    3,   8],
    [INF, INF, 3,    0,    5],
    [INF, 6,    8,    5,   0]
]
nearest = [-1] * (n + 1)
distance = [-1] * (n + 1)

F = prim(n, W)
for edge in F:
    print(edge)
