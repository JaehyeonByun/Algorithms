def exchangesort(n, S):

    for i in range(n-1):
        for j in range(i+1,n):          
            if(S[j] < S[i]):
                S[j], S[i] = S[i], S[j]
# Example 1
print("######Example 1######") 
S = [10, 7, 11, 5, 13, 8]
exchangesort(len(S), S)
print("sorted S:", S)
print(f"{'-'*20}\n")

# Example 2
print("######Example 2######") 
S = [10,9,8,7,6,5,4,3,2,1]
exchangesort(len(S), S)
print("sorted S:", S)
print(f"{'-'*20}\n")

# Example 3 - Your Custom Case 
print("######Example 3######") 
# Insert your example here
S = [4,3,2,1,5,6,10,33,22,14] 
exchangesort(len(S), S)
print("sorted S:", S)
print(f"{'-'*20}\n")