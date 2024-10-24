import math

def binsearch(n, S, x):
    low, high = 0, n-1
    location = -1
    while(low <= high and location == -1):
        mid = math.floor((low + high) / 2)
        if(x == S[mid]):
            location = mid
        elif (x < S[mid]):
            high = mid - 1
        else:
            low = mid + 1

    return location

# Example 1
print("######Example 1######")
S = [5, 7, 8, 10, 11, 13]
x = 15 
location = binsearch(len(S), S, x)
print("location:", location)
print(f"{'-'*20}\n")

# Example 2
print("######Example 2######") 
S = [5, 7, 8, 10, 11, 13]
x = 10 
location = binsearch(len(S), S, x)
print("location:", location)
print(f"{'-'*20}\n")

# Example 3 - Your Custom Case 
print("######Example 3######") 
# Insert your example here
S = [1, 2, 5, 9, 15, 21, 33, 52, 100]
x = 100
location = binsearch(len(S), S, x)
print("location:", location)
print(f"{'-'*20}\n")