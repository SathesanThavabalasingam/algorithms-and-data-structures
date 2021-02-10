# Write a function called sumZero which accepts a sorted
# array of integers. The function should find the first pair where 
# the sum is 0.

def sumZero(arr):
    left = 0
    right = len(arr) - 1
    while (left < right):
        sums = arr[left] + arr[right]
        if sums == 0:
            return [arr[left],arr[right]]
        elif sums > 0:
            right-=1
        else:
            left+=1

sumZero([-4,-3,-2,-1,0,1,2,3,19])