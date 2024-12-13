def knapsack(n, W, w, p):
    P = [[0]*(W+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for wt in range(W+1):
            if w[i] <= wt:
                P[i][wt] = max(P[i-1][wt], p[i] + P[i-1][wt - w[i]])
            else:
                P[i][wt] = P[i-1][wt]

    return P[n][W]

# 예제 1
print("######Example 1######")
n, W = 3, 30
w = [0, 5, 10, 20]  
p = [0, 50, 60, 140] 
maxprofit = knapsack(n, W, w, p)
print("maxprofit: ", maxprofit)

# 예제 2 (사용자 정의 예제)
print("######Example 2 #######")
n, W = 4, 50
w = [0, 10, 20, 30, 40]
p = [0, 60, 100, 120, 240]
maxprofit = knapsack(n, W, w, p)
print("maxprofit: ", maxprofit)
