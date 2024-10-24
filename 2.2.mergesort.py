def merge(h, m, U, V, S):
    assert sorted(U) == U
    assert sorted(V) == V
    
    i = j = k = 0

    while i < h and j < m:
        if(U[i] < V[j]):
            S[k] = U[i]
            i += 1
        else:
            S[k] = V[j]
            j += 1
        k += 1
    
    if(i >= h):
        for _ in range(j,m):
            S[k] = V[_]
            k += 1
    else:
        for _ in range(i,h):
            S[k] = U[_]
            k += 1
        
def mergesort(n, S):
    h = n // 2
    m = n - h
    if n > 1:
        U = S[:h]
        V = S[h:]
        for j in range(m):
            V[j] = S[j+h]    
        mergesort(h,U)
        mergesort(m,V)
        merge(h,m,U,V,S)

# Example 1 for 'merge()'
print("######Example 1 for 'merge()'######")
U = [17, 19, 39, 41, 73] # sorted
V = [16, 22, 66, 94, 98] # sorted
h = len(U)
m = len(V)
S = [-1] * (h + m)
merge(h, m, U, V, S)
print("S:", S)
print(f"{'-'*20}\n")

# Example 2 - Your Custom Case for 'merge()'
print("######Example 2 for 'merge()'######") 
# Insert your example here
U = [16, 22, 66, 94, 98] # sorted
V = [17, 19, 39, 41, 73] # sorted
h = len(U)
m = len(V)
S = [-1] * (h + m)
merge(h, m, U, V, S)
print("S:", S)
print(f"{'-'*20}\n")

# Example 1 for 'mergesort()'
print("######Example 1 for 'mergesort()'######")
S = [22, 98, 17, 16, 19, 73, 94, 41, 39, 66]
mergesort(len(S), S)
print("S:", S)
print(f"{'-'*20}\n")

# Example 2 - Your Custom Case for 'mergesort()'
print("######Example 2 for 'mergesort()'######") 
# Insert your example here
S = [1, 8, 17, 10, 4, 9, 111, 62]
mergesort(len(S), S)
print("S:", S)
print(f"{'-'*20}\n")
