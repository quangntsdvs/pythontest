def printUnorderedPairs(arrayA, arrayB): 
    for i in range(len(arrayA)): 
        for j in range(len(arrayB)): 
            for k in range(0,100000): 
                print(str(arrayA[i]) + "," + str(arrayB[j]))
#Kết quả sẽ là một lượng lớn dữ liệu, vì mỗi cặp sẽ được in ra 100,000 lần