def printPairs(array):
    # Lặp qua từng phần tử i trong mảng
    for i in array:
        # Lặp qua từng phần tử j trong mảng
        for j in array:
            # In ra cặp giá trị (i, j)
            print(str(i)+","+str(j))

#ví dụ:
input_array = [4, 8 ,9, 10]
printPairs(input_array)