def countUniqueValues(arr):
    # initiate first pointer
    i=0
    # loop over second lead pointer to the right of i
    for j in range(1,len(arr)):
        # if i and j are not equal then i is pushed forward 
        # and takes the current value of j. Otherwise i stays in place.
        # we are pushing all unique values to the front of the array.
        if arr[i] != arr[j]:
            i+=1
            arr[i] = arr[j]
        print([i,j])
    # return i plus 1 to get the number of the unique values        
    return i + 1

countUniqueValues([1,1,1,2,3,3,4,4,5,6])
countUniqueValues([1,1,1,2,3,3,4,5,6,99,105])
    