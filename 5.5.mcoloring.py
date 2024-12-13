def promising(i):
    global W, vcolor, n
    for j in range(1, i):
        if W[i][j] == 1 and vcolor[i] == vcolor[j]:
            return False
    return True

def mcoloring(i, m):
    global n, vcolor, count
    if promising(i):
        if i == n:
            print(vcolor[1:])
            count += 1
        else:
            for color in range(1, m+1):
                vcolor[i+1] = color
                mcoloring(i+1, m)

# Example 1
print("######Example 1######")
m = 3
n = 4
count = 0
vcolor = [0] * (n + 1)
W = [[0,0,0,0,0],
     [0,0,1,1,1], 
     [0,1,0,1,0], 
     [0,1,1,0,1],
     [0,1,0,1,0]] 
mcoloring(0, m)
print("count =",count)

# Example 2 - Your Custom Case
print("######Example 2 #######")
m = 2
n = 5
count = 0
vcolor = [0] * (n + 1)

W = [[0,0,0,0,0,0],
     [0,0,1,1,1,1],
     [0,1,0,0,0,0],
     [0,1,0,0,0,0],
     [0,1,0,0,0,0],
     [0,1,0,0,0,0]]

mcoloring(0, m)
print("count =",count)
