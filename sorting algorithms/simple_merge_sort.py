def simple_mergesort(arr1, arr2):
    sorted_list = []
    len_arr1 = len(arr1)
    len_arr2 = len(arr2)
    i = j = 0

    while i < len_arr1 and j < len_arr2:
        if arr1[i] <= arr2[j]:
            sorted_list.append(arr1[i])
            i += 1 
        else:
            sorted_list.append(arr2[j])
            j += 1

    while i < len_arr1:
        sorted_list.append(arr1[i])
        i += 1
    while j < len_arr2:
        sorted_list.append(arr2[j])
        j += 1
    
    return sorted_list


arr1 = [1,2,6,9]
arr2 = [3,4,7,8]
print(simple_mergesort(arr1, arr2))