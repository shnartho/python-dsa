def bubble_sort(arr):
    length = len(arr)
    for i in range(length):
        swapped = False
        for j in range(length-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        # amon jodi hoy je pura akta i valuer somoy dekhlo pura arr tai sort kora tahole to ar amar bar bar check korar proyojon nai. Tahole ami just break kore ber hoye jabo. se jonno swapper var use kora hoyeche.

        if not swapped:
            break

arr = [64, 55, 13, 1, 23, 22, 34, 15]
bubble_sort(arr)
print("Sorted array is: ", arr)
