def arrsum(n, S):
    result = 0
    for i in range(n):
        result += S[i]

    return result

# Example 1
print("######Example 1######") 
S = [10, 7, 11, 5, 13, 8]
sum = arrsum(len(S), S)
print("sum:", sum)
print(f"{'-'*20}\n")

# Example 2
print("######Example 2######") 
S = list(range(100))
sum = arrsum(len(S), S)
print("sum:", sum)
print(f"{'-'*20}\n")

# Example 3 - Your Custom Case 
print("######Example 3######") 
# Insert your example here
S = [10, 555, 44, 1, 15, 4]
sum = arrsum(len(S), S)
print("sum:", sum)
print(f"{'-'*20}\n")