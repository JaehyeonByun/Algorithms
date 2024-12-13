def knapsack(n, W, DP):
    global w, p
    if n == 0 or W <= 0:
        DP[(n, W)] = 0
    else:
        if w[n] > W:
            DP[(n, W)] = knapsack(n - 1, W, DP) 
        else:
            DP[(n, W)] = max(knapsack(n - 1, W, DP), 
                             knapsack(n - 1, W - w[n], DP) + p[n])

    return DP[(n, W)]

# Example 1
print("######Example 1######")
n, W = 3, 30
w = [0, 5, 10, 20]
p = [0, 50, 60, 140]
DP = {}
maxprofit = knapsack(n, W, DP)
print("maxprofit: ", maxprofit)

# Example 2 - Your Custom Case
print("######Example 2 #######") 
# Insert your example here
n, W = 3, 50
w = [0, 5, 10, 20]
p = [0, 50, 60, 140]
DP = {}
maxprofit = knapsack(n, W, DP)
print("maxprofit: ", maxprofit)