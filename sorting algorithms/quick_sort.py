def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()

    items_greater = []
    items_smaller = []

    for item in arr:
        if item > pivot:
            items_greater.append(item)
        else:
            items_smaller.append(item)
        
    return quick_sort(items_smaller) + [pivot] + quick_sort(items_greater)

print(quick_sort([5,3,4,8,1,9,33,11]))
    