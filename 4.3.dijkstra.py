def dijkstra(n, W):
    F = []
    for i in range(2, n + 1):
        touch[i] = 1
        length[i] = W[1][i]
    
    for _ in range(n - 1):
        min_length = INF
        vnear = -1

        for i in range(2, n + 1):
            if 0 <= length[i] < min_length:
                min_length = length[i]
                vnear = i

        F.append((touch[vnear], vnear, W[touch[vnear]][vnear]))

        length[vnear] = -1

        for i in range(2, n + 1):
            if W[vnear][i] < INF and (length[i] > min_length + W[vnear][i]):
                length[i] = min_length + W[vnear][i]
                touch[i] = vnear

    return F

INF = float("inf")

# Example 1
print("######Example 1######")
n = 5 # the number of vertices
W = [ # adjacency matrix
        [INF,    INF,      INF,    INF,      INF,      INF],
        [INF,      0,        7,      4,        6,        1],
        [INF,    INF,        0,     INF,     INF,      INF],
        [INF,    INF,        2,      0,        5,      INF],
        [INF,    INF,        3,    INF,        0,      INF],
        [INF,    INF,      INF,    INF,        1,        0]
    ]
touch = [-1] * (n + 1)
length = [-1] * (n + 1)

F = dijkstra(n, W)
for edge in F:
    print(edge)


# Example 2 - Custom Case
print("######Example 2 #######")
n = 4
W = [
    [INF, INF, INF, INF, INF],
    [INF, 0,    10,    15,   20],
    [INF, INF,  0,    INF,    5],
    [INF, INF,  5,      0,   10],
    [INF, INF, INF,    INF,    0]
]
touch = [-1] * (n + 1)
length = [-1] * (n + 1)

F = dijkstra(n, W)
for edge in F:
    print(edge)
