def selectionSort(arr):
    for i in range(len(arr) - 1):
        lowest = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[lowest]:
                lowest = j
        temp = arr[i]
        arr[i] = arr[lowest]
        arr[lowest] = temp
    return arr

selectionSort([34,22,10,19,17])