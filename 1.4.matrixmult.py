def matrixmult(n, A, B):
    C = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] = C[i][j] + A[i][k] * B[k][j]

    return C

# Example 1
print("######Example 1######") 
A = [[2, 3],[4, 1]]
B = [[5, 7],[6, 8]]
C = matrixmult(len(A), A, B)
print("C:", C)
print(f"{'-'*20}\n")

# Example 2
print("######Example 2######") 
A = [[1, 2],[3, 4]]
B = [[4, 1],[1, 0]]
C = matrixmult(len(A), A, B)
print("C:", C)
print(f"{'-'*20}\n")

# Example 3 - Your Custom Case 
print("######Example 3######") 
# Insert your example here
A = [[3, 5],[1, 4]]
B = [[2, 1],[10, 0]]
C = matrixmult(len(A), A, B)
print("C:", C)
print(f"{'-'*20}\n")