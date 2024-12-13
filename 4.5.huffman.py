from heapq import heappush, heappop

class Node:
    def __init__(self, symbol, freq):
        self.symbol = symbol
        self.freq = freq
        self.left = '+'
        self.right = '+'

    def preorder(self, path):
        path.append((self.symbol, self.freq))
        if self.left != '+':
            self.left.preorder(path)
        if self.right != '+':
            self.right.preorder(path)

    def inorder(self, path):
        if self.left != '+':
            self.left.inorder(path)
        path.append((self.symbol, self.freq))
        if self.right != '+':
            self.right.inorder(path)

def huffman(n, s, f):
    heap = []
    for i in range(n):
        heappush(heap, (f[i], Node(s[i], f[i])))

    # Huffman Algorithm
    while len(heap) > 1:
        f1, n1 = heappop(heap)
        f2, n2 = heappop(heap)
        new_node = Node('+', f1 + f2)
        new_node.left = n1
        new_node.right = n2
        heappush(heap, (new_node.freq, new_node))
    
    return heappop(heap)[1]

# Example 1
print("######Example 1######")
n = 6
s = ['b', 'e', 'c', 'a', 'd', 'f']
f = [5, 10, 12, 16, 17, 25]
root = huffman(n, s, f)
path = []
root.preorder(path)
print("preorder= ",path)
path = []
root.inorder(path)
print("inorder= ",path)


# Example 2 - Custom Case
print("######Example 2 #######")
n = 4
s = ['x', 'y', 'z', 'w']
f = [10, 3, 5, 9]
root = huffman(n, s, f)
path = []
root.preorder(path)
print("preorder= ",path)
path = []
root.inorder(path)
print("inorder= ",path)
