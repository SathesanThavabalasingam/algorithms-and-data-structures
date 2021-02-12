# Given a sorted array find the index of a number in it.
def searchArray(arr, num):
    min = 0
    max = len(arr)-1

    while (min <= max):
        mid = round((min+max)/2)
        
        if arr[mid] < num:
            min = mid + 1
        elif arr[mid] > num:
            max = mid- 1
        else:
            return mid

searchArray([1,2,3,4,5,6,9,55],4)
