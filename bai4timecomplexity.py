def findBiggestNumber(sampleArray): 
    # Khởi tạo giá trị lớn nhất là phần tử đầu tiên của mảng
    biggestNumber = sampleArray[0]
    # Duyệt qua các phần tử từ index 1 đến hết mảng
    for index in range(1,len(sampleArray)):
        # So sánh giá trị tại vị trí index với giá trị lớn nhất hiện tại
        if sampleArray[index] > biggestNumber:
            biggestNumber = sampleArray[index]
    # In ra giá trị lớn nhất
    print(biggestNumber)
# sampleArray:
sampleArray = [5, 4, 10, 8, 11, 68, 78]
# Gọi hàm để tìm và in ra giá trị lớn nhất trong mảng
findBiggestNumber(sampleArray)