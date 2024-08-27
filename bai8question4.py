# Hàm in các cặp phần tử không theo thứ tự từ hai mảng
def printUnorderedPairs(arrayA, arrayB): 
    # Duyệt qua các phần tử của arrayA
    for i in range(len(arrayA)): 
        # Duyệt qua các phần tử của arrayB
        for j in range(len(arrayB)):
            # Kiểm tra nếu phần tử từ arrayA nhỏ hơn phần tử từ arrayB 
            if arrayA[i] < arrayB[j]: 
                # In ra cặp phần tử không theo thứ tự
                print(str(arrayA[i]) + "," + str(arrayB[j]))

# Ví dụ:
array1 = [1, 2, 3, 4, 5]
array2 = [6, 7, 8, 9, 10]
print("Unordered pairs")
printUnorderedPairs(array1, array2)