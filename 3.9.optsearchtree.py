class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
    
    def preorder(self, path):
        path.append(self.key)
        if self.left != None:
            self.left.preorder(path)
        if self.right != None:
            self.right.preorder(path)

    def inorder(self, path):
        if self.left != None:
            self.left.inorder(path)
        path.append(self.key)
        if self.right != None:
            self.right.inorder(path)

def minimum(i, j, A, p):
    minvalue, mink = INF, 0
    total_prob = sum(p[i:j + 1])
    
    for k in range(i, j + 1):
        cost = A[i][k - 1] + A[k + 1][j] + total_prob
        if cost < minvalue:
            minvalue = cost
            mink = k
    
    return minvalue, mink

def optsearchtree(n, p):
    A = [[INF] * (n + 1) for _ in range(n + 2)]
    R = [[0] * (n + 1) for _ in range(n + 2)]
    
    for i in range(1, n + 1):
        A[i][i - 1] = R[i][i - 1] = 0
        A[i][i], R[i][i] = p[i], i
    
    A[n + 1][n] = R[n + 1][n] = 0
    
    for diagonal in range(1, n):
        for i in range(1, n - diagonal + 1):
            j = i + diagonal
            A[i][j], R[i][j] = minimum(i, j, A, p)
    
    return A[1][n], A, R

def tree(i, j, K, R):
    k = R[i][j]
    if k == 0:
        return None
    else:
        root = Node(K[k])
        root.left = tree(i, k - 1, K, R)
        root.right = tree(k + 1, j, K, R)
        return root

INF = float("inf")

# Example 1
print("######Example 1######")
n = 4
K = [0, 10, 20, 30, 40]
p = [0, 3, 3, 1, 1]
minavg, A, R = optsearchtree(n, p)
print("A = ")
for i in range(1, n + 2):
    print(A[i][i-1:])
print("R = ")
for i in range(1, n + 2):
    print(R[i][i-1:])
print("minavg = ", minavg)

root = tree(1, n, K, R)
path = [] 
root.preorder(path)
print("preorder=", path)
path = []
root.inorder(path)
print("inorder=", path)

# Example 2 - Custom Case
print("######Example 2 #######")
n = 5  
K = [0, 5, 15, 25, 35, 45]  
p = [0, 2, 5, 3, 4, 1]  

minavg, A, R = optsearchtree(n, p)
print("A = ")
for i in range(1, n + 2):
    print(A[i][i-1:])
print("R = ")
for i in range(1, n + 2):
    print(R[i][i-1:])
print("minavg = ", minavg)

root = tree(1, n, K, R)
path = [] 
root.preorder(path)
print("preorder=", path)
path = []
root.inorder(path)
print("inorder=", path)