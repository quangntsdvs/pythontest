def fibonacci(n, memo={}):
    # Kiểm tra xem n đã được tính toán trước đó chưa
    if n in memo:
        return memo[n]

    # Trường hợp cơ bản: nếu n là 0 hoặc 1, trả về n
    if n <= 1:
        result = n
    else:
        # Gọi đệ quy để tính F(n-1) và F(n-2)
        result = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    # Lưu kết quả vào memo để sử dụng lại lần sau    
    memo[n] = result
    return result
# ví dụ:
n = 10
result = fibonacci(n)
print(f"The {n}-th Fibonacci number is: {result}")
