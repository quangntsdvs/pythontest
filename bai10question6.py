def reveverse (array): 
    for i in range(0, int(len(array)/2)):
        other = len(array)-i-1
        temp = array[i]
        array[i] = array[other]
        array[other] = temp
    print(array)
#ví dụ:
array = [1, 2, 3, 4, 5]
reveverse(array)