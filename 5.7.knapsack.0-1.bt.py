def promising(i, weight, profit):
    global n, W, w, p, maxprofit
    if weight >= W:
        return False
    total_weight = weight
    bound = profit
    j = i + 1
    while j <= n and total_weight + w[j] <= W:
        total_weight += w[j]
        bound += p[j]
        j += 1
    if j <= n:
        bound += (W - total_weight) * (p[j] / w[j])

    return bound > maxprofit


def knapsack(i, weight, profit):
    global n, W, w, p, bestset, include, maxprofit
    if weight <= W and profit > maxprofit:
        maxprofit = profit
        for k in range(1, n + 1):
            bestset[k] = include[k]

    if i < n and promising(i, weight, profit):
        include[i + 1] = 1  
        knapsack(i + 1, weight + w[i + 1], profit + p[i + 1])
        include[i + 1] = 0 
        knapsack(i + 1, weight, profit)

# Example 1
print("######Example 1######")
n, W = 4, 16
w = [0] + [2, 5, 10, 5]
p = [0] + [40, 30, 50, 10]
bestset, include = [0] * (n + 1), [0] * (n + 1)
maxprofit = 0
knapsack(0, 0, 0)
print("maxprofit =", maxprofit)
print("bestset =", bestset)


# Example 2 - Your Custom Case
print("######Example 2 #######")
n, W = 5, 15
w = [0] + [1, 3, 4, 7, 8]
p = [0] + [5, 6, 10, 12, 13]
bestset, include = [0] * (n + 1), [0] * (n + 1)
maxprofit = 0
knapsack(0, 0, 0)
print("maxprofit =", maxprofit)
print("bestset =", bestset)
