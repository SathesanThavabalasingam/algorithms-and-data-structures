def bubbleSort(arr):
    for i in range(len(arr)-1):
        # second loop starts from 0 but limits to i each time to make sure we don't keep
        # going unecessarily
        for j in range(len(arr)-1 -i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr
            
bubbleSort([37,45,29,8])