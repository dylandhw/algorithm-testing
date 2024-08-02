def bubble_sort(arr):
    n = len(arr)
    #navigate through list
    for i in range(n):
        #last i elements are already sorted
        for j in range(0, n-i-1):
            #navigate the list from 0 to n-i-1
            #swap
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

#output 
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("array post sort:", arr)
