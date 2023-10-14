def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i +1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

arr = [3,1,22,13,4,11,6,2,9]
selection_sort(arr)
print("Sorted array is: ", arr)