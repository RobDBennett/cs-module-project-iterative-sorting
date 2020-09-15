# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        smallest_index = i
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j
        # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

"""
Teacher's solution.
def bubble_sort(arr):
    swaps_occurred = True
    while swaps_occurred:
        swaps_occurred = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swaps_occurred = True
    return arr
"""

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''


def counting_sort(arr, maximum=None):
    """
    This function executes a counting sort. The first three
    if statements are for testing specific circumstances.
    maximum represents the highest value in the array. If this value
    is provided, we operate with it. Otherwise we execute a max() on the 
    of the given array to find it.
    We then create an array of 0's equal to the max value +1. Then a 
    for loop is executed which creates 'buckets' of each count of values.
    We instantiate an index count, and then execute a nested for loop that
    goes through a range equal to the max+1, and then through the range of the 
    each item of the count. 
    Finally, the array index is altered to place the numbers properly, 
    and the index counter is increased.
    """
    if maximum == None and len(arr) != 0:
        maximum = max(arr)  # Alters Maximum away from default None.
    if arr == []:
        return arr  # Checks if the array is empty before sorting.
    if min(arr) < 0:  # Checks that each item is positive.
        return "Error, negative numbers not allowed in Count Sort"

    m = maximum + 1  # Add a value to ensure python gets to the proper number.
    # Create a list of 0s equal to the maximum value +1 (to account for 0)
    count = [0] * m
    for a in arr:  # Loop through the array, adding to count index each time that value appears.
        count[a] += 1

    i = 0  # Instantiate a separate counter.
    for a in range(m):  # Loop through the range of 0 to the max +1
        for c in range(count[a]):  # Loop through the items in the count array
            # Replaces the starting array element by element so that the order reflects the index counter and array value.
            arr[i] = a
            i += 1

    return arr

"""
Teacher's solution:
def counting_sort(arr, maximum=None):
    if maximum is None:
        maximum = max(arr)
    buckets = [0 for i in range(maximum + 1)]
    for value in arr:
        if value < 0:
            return "Error, negative numbers not allowed in Count Sort"
        buckets[value] += 1

    output = []
    for indext, bucket in enumerate(buckets):
        output.extend([index for i in range(count)])
    return output

"""
#    if maximum == None:
#        maximum = len(arr)
#    counts = [0] * ((maximum) + 1)
#    for item in arr:
#        if item >= 0:
#            counts[item] += 1
#        else:
#            return "Error, negative numbers not allowed in Count Sort"
#
#    num_items_before = 0
#    for i, count in enumerate(counts):
#        counts[i] = num_items_before
#        num_items_before += count
#
#    sorted_list = [None] * len(arr)
#    for item in arr:
#        sorted_list[ counts[item] ] = item
#        counts[item] += 1
#    return sorted_list

#    size = len(arr)
#    output = [0] * size
#    count = [0] * 10
#    for i in range(0, size):
#        count[arr[i]] += 1
#
#    for i in range(1, 10):
#        count[i] += count[i-1]
#
#    i = size - 1
#    while i >= 0:
#        if arr[i] >= 0:
#            output[count[arr[i]] - 1 ] = arr[i]
#            count[arr[i]] -= 1
#            i -= 1
#        else:
#            return "Error, negative numbers not allowed in Count Sort"
#
#    for i in range(0, size):
#        arr[i] = output[i]
#
#    return arr
