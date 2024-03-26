array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quickSort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[len(array) // 2]
    small, equal, big = [], [], []
    for i in array:
        if i < pivot:
            small.append(i)
        elif i > pivot:
            big.append(i)
        else:
            equal.append(i)
    
    return quickSort(small) + equal + quickSort(big)

print(quickSort(array))