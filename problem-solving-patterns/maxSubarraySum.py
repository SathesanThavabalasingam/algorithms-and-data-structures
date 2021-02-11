# Write a function called maxSubarraySum which accepts an array of integers
# and a number called n. The function should calculate the maximum sum of n 
# consecutive elements in the array.

def maxSubarraySum(arr, num):
    maxSum = 0
    tempSum = 0
    if len(arr) < num:
        return []
    # create the first window and sum of each element in that window
    for i in range(num):
        maxSum += arr[i]
    tempSum = maxSum
    for i in range(num, len(arr)):
        # new sum is created for new window by subtracting first val of last window
        # and adding last val of new window
        tempSum = tempSum - arr[i-num] + arr[i]
        # check which window sum is the largest and store.
        maxSum = max(maxSum, tempSum)
    return maxSum

maxSubarraySum([2,6,9,2,1,8,5,6,3],3)
