def factorial (n): 
    if n <0: 
        return -1 
    elif n == 0: 
        return 1
    else:
        return n * factorial (n-1)
# ví dụ:
example_number = 6
result = factorial(example_number)
print(f"The factorial of {example_number} is: {result}")