def bubbleSort(array):
    for i in range(0,len(array) - 1):
        for j in range(0,(len(array) - i - 1)):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

    print(array)


a = [0,5,2,3,1,7,0]

bubbleSort(a)
