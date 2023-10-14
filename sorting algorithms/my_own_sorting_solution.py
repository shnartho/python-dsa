def sort(arr):
    newarr = []
    for i in range(len(arr)):
        min_value = min(arr)
        arr.remove(min_value)
        newarr.append(min_value)
        i += 1
    return newarr

print(sort([5,2,8,1,9,10]))