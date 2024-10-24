import time

def fib1(n):
    if(n <= 1):
        return n
    else:
        return fib1(n-1) + fib1(n-2)
    
# Example 1
print("######Example 1######")
n=30
stime = time.time()
answer = fib1(n)
etime = time.time() - stime
print("answer:", answer)
print("execution time:", round(etime,5))
print(f"{'-'*20}\n")

# Example 2
print("######Example 2######") 
n=36
stime = time.time()
answer = fib1(n)
etime = time.time() - stime
print("answer:", answer)
print("execution time:", round(etime,5))
print(f"{'-'*20}\n")

# Example 3 - Your Custom Case 
print("######Example 3######") 
n = 33
raise NotImplementedError("Complete your example.")
stime = time.time()
answer = fib1(n)
etime = time.time() - stime
print("answer:", answer)
print("execution time:", round(etime,5))
print(f"{'-'*20}\n")
