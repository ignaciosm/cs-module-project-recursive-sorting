# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements

    print('arrA', arrA)
    print('arrB', arrB)

    a = 0
    b = 0
    
    for i in range(0, elements):
        if a >= len(arrA):
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):
            merged_arr[i] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:
            merged_arr[i] = arrA[a]
            a += 1
        else:
            merged_arr[i] = arrB[b]
            b += 1

    return merged_arr

# left = [0, 1, 2, 3, 4]
# right = [5, 6, 7, 8, 9]
# print(merge(left,right))


arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
arr2 = [1, 5, 8, 4]
arr3 = [1, 5]
# arr4 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

# # TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len(arr) == 0:
        return arr
    # base case
    if len(arr) == 1:
        # print('base:',arr[0])
        return arr
    # define mid
    mid = len(arr) // 2
    # slice < to left, > to right
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    # call merge helper
    arr = merge(left, right)
     
    return arr

print(merge_sort(arr2))



# # STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# # utilize any extra memory
# # In other words, your implementation should not allocate any additional lists 
# # or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here

