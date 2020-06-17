# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # SORT LIST
    # define base case: if bucket is 0 or 1, return bucket
    # if len(arr) == 0:
    #     return arr
    # if length == 1:
    #     return arr
    # # define a midpoint and empty left and right buckets
    # mid = len(arr) // 2
    # left = []
    # right = []    
    # # if element <= than midpoint, then left... if > then right
    # # if element <= than midpoint, then left... if > then right
    # for i in range(start, end):
    #     if arr[i] <= arr[mid]:
    #         left.append(arr[i])
    #         return binary_search(left, target, 0, len(left)-1)
    #     else:
    #         right.append(arr[i])
    #         return binary_search(right, target, 0, len(right)-1)
    # return 


    # SEARCH A SORTED LIST

    # if array empty
    if len(arr) == 0:
        return -1 # why -1? and not None?
    # define midpoint of search range
    mid = (start + end) // 2
    # base case
    # if len(arr) == 1 and arr[mid] == target:
    #     return mid
    # else:
    #     return None
    # if we're lucky and target is exactly mid
    if arr[mid] == target:
        return mid
    # run recursive search on the lower half
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid-1)
    # run recursive search on the higher half        
    else:
        return binary_search(arr, target, mid+1, end)

arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
print(binary_search(arr1, 3, 0, len(arr1)))    # how to add response for a number that is not found in the list?
    

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
    # Your code here

