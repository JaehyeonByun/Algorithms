def promising(i, weight, total):
    global n, W, w, include
    if (weight + total >= W) and (weight == W or (i+1 <= n and weight + w[i+1] <= W)):
        return True
    return False

def sumofsubsets(i, weight, total):
    global n, W, w, include
    if promising(i, weight, total):
        if weight == W:
            print("found:", include[1:])
        else:
            if i+1 <= n:
                include[i+1] = 1
                sumofsubsets(i+1, weight + w[i+1], total - w[i+1])

                include[i+1] = 0
                sumofsubsets(i+1, weight, total - w[i+1])

print("######Example 1######")
n, W = 4, 13
w = [0, 3, 4, 5, 6] 
include = [0] * (n + 1)
sumofsubsets(0, 0, sum(w[1:]))

print("######Example 2 #######")
n, W = 5, 10
w = [0, 2, 3, 4, 5, 6]
include = [0] * (n + 1)
sumofsubsets(0, 0, sum(w[1:]))
