import time
def fib2(n):
    f = [0] * (n + 1)
    if (n>0):
        f[1] = 1
        for i in range(2,n+1):
            f[i] = f[i-1] + f[i-2]

    return f[n]

# Example 1
print("######Example 1######")
n=30
stime = time.time()
answer = fib2(n)
etime = time.time() - stime
print("answer:", answer)
print("execution time:", round(etime,5))
print(f"{'-'*20}\n")

# Example 2
print("######Example 2######") 
n=36
stime = time.time()
answer = fib2(n)
etime = time.time() - stime
print("answer:", answer)
print("execution time:", round(etime,5))
print(f"{'-'*20}\n")

# Example 3 - Your Custom Case 
print("######Example 3######") 
# Insert your example here
n = 40
stime = time.time()
answer = fib2(n)
etime = time.time() - stime
print("answer:", answer)
print("execution time:", round(etime,5))
print(f"{'-'*20}\n")