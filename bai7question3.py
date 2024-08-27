def printUnorderedPairs(array): 
    # Lặp qua từng phần tử i trong mảng
    for i in range(0, len(array)): 
        # Lặp qua từng phần tử j trong mảng, bắt đầu từ vị trí (i+1)
        for j in range(i + 1, len(array)): 
            # In ra cặp giá trị (array[i], array[j])
            print(str(array[i]) + "," + str(array[j]))

# Ví dụ sử dụng:
input_array = [7, 2, 8]
printUnorderedPairs(input_array)
