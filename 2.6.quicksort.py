def partition(low, high, S):
    pivotitem = S[low]
    j = low
    for i in range(low+1,high+1):
        if(S[i] < pivotitem):
            j += 1
            S[i],S[j] = S[j],S[i]
    pivotpoint = j
    S[low],S[pivotpoint] = S[pivotpoint],S[low]
    return pivotpoint

def quicksort(low, high, S):
    if low < high:
        pivotpoint = partition(low, high, S)
        quicksort(low, pivotpoint-1, S)
        quicksort(pivotpoint+1, high, S)
        
# Example 1 for 'partition()'
print("######Example 1 for 'partition()'######")
S = [17, 19, 39, 41, 73] # sorted in ascending order
pivotpoint = partition(0, len(S) - 1, S)
print(f"Left Sub-S: {S[:pivotpoint]}, pivotitem={S[pivotpoint]}, Right Sub-S: {S[pivotpoint+1:]}")
print(f"{'-'*20}\n")

# Example 2 for 'partition()'
print("######Example 2 for 'partition()'######")
S = [73, 41, 39, 19, 17] # sorted in descending order
pivotpoint = partition(0, len(S) - 1, S)
print(f"Left Sub-S: {S[:pivotpoint]}, pivotitem={S[pivotpoint]}, Right Sub-S: {S[pivotpoint+1:]}")
print(f"{'-'*20}\n")

# Example 3 for 'partition()'
print("######Example 3 for 'partition()'######")
S = [39, 41, 19, 74, 17] # not sorted
pivotpoint = partition(0, len(S) - 1, S)
print(f"Left Sub-S: {S[:pivotpoint]}, pivotitem={S[pivotpoint]}, Right Sub-S: {S[pivotpoint+1:]}")
print(f"{'-'*20}\n")

# Example 4 - Your Custom Case for 'partition()'
print("######Example 4 for 'partition()'######") 
# Insert your example here
S = [7,5,12,9,53,12,4,73,21,77]
pivotpoint = partition(0, len(S) - 1, S)
print(f"Left Sub-S: {S[:pivotpoint]}, pivotitem={S[pivotpoint]}, Right Sub-S: {S[pivotpoint+1:]}")
print(f"{'-'*20}\n")

# Example 1 for 'quicksort()'
print("######Example 1 for 'quicksort()'######")
S = [22, 98, 17, 16, 19, 73, 94, 41, 39, 66]
quicksort(0, len(S)-1, S)
print("S:", S)
print(f"{'-'*20}\n")

# Example 2 - Your Custom Case for 'quicksort()'
print("######Example 2 for 'quicksort()'######") 
# Insert your example here
S = [10,63,4,32,96,74,38,12] 
quicksort(0, len(S)-1, S)
print("S:", S)
print(f"{'-'*20}\n")
