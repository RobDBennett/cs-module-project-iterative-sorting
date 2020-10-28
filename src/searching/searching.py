def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    left = 0
    right = len(arr) - 1
    while left <= right:
        midpoint = (right + left) // 2
        if arr[midpoint] == target:
            return midpoint
        elif arr[midpoint] < target:
            #Get rid of everything on the left.
            left = midpoint + 1
        else:
            right = midpoint - 1

    return -1  # not found
#Constant space complexity. Variables don't count. O(n)
#O(log(n))