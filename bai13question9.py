def allFib(n): 
    for i in range (n): 
        print(str(i)+":, " + str(fib(i)))

def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

# Chạy ví dụ với n = 6
example_n = 6
allFib(example_n)