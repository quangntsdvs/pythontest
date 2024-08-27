# Hàm để phân vùng mảng và trả về chỉ mục phân vùng
def partition(arr, low, high):
    i = (low - 1)       # chỉ mục của phần tử nhỏ hơn
    pivot = arr[high]   # phần tử chốt

    for j in range(low, high):
        # Nếu phần tử hiện tại nhỏ hơn phần tử chốt
        if arr[j] < pivot:
            # Tăng chỉ mục của phần tử nhỏ hơn
            i = i + 1
            # Hoán đổi arr[i] và arr[j]
            arr[i], arr[j] = arr[j], arr[i]

    # Hoán đổi phần tử chốt với phần tử ở vị trí đúng
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Hàm để thực hiện thuật toán QuickSort
def quickSort(arr, low, high):
    if low < high:
        # pi là chỉ mục phân vùng, arr[pi] hiện nay ở đúng vị trí
        pi = partition(arr, low, high)

        # Sắp xếp đệ quy các mảng con trước và sau phân vùng
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

# Mã điều khiển để kiểm tra việc triển khai QuickSort
arr = [6, 3, 9, 8, 5]
n = len(arr)
quickSort(arr, 0, n - 1)

# In mảng đã sắp xếp
print("Mảng sau khi sắp xếp là:")
for i in range(n):
    print("%d" % arr[i])