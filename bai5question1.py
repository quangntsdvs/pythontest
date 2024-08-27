def foo(array):
    # Khởi tạo sum và product
    sum = 0
    product = 1
    # Tính tổng
    for i in array:
        sum += i
    # Tính tích
    for i in array:
        product *= i
    # In ra tổng và tích
    print("Sum = " + str(sum) + ", Product = " + str(product))
# ví dụ:
input_array = [1, 2, 3, 4, 5]
foo(input_array)