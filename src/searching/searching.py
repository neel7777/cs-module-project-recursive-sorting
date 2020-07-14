# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    middle = (start + end) // 2

    if end < start:
        return -1

    
    if target == arr[middle]:
        return middle
    elif target < arr[middle]:
        end = middle - 1
        return binary_search(arr, target, start, end)
    elif target > arr[middle]:
        start = middle + 1
        return binary_search(arr, target, start, end)
                


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
    # Your code here

