inversions_count = 0

def mergeSort(arr):
    global inversions_count
    if len(arr) > 1:
        mid = len(arr) // 2
        arrLeft = arr[:mid]
        arrRight = arr[mid:]
        mergeSort(arrLeft)
        mergeSort(arrRight)
        print(arrLeft,arrRight,arr)
        merge(arrLeft, arrRight, arr)

def merge(arrLeft, arrRight, arr):
    global inversions_count
    i = j = k = 0
    
    while i < len(arrLeft) and j < len(arrRight):
        print("arr",arr)
        if arrLeft[i] <= arrRight[j]:
            arr[k] = arrLeft[i]
          
            i += 1
        else:
            arr[k] = arrRight[j]
            j += 1
            inversions_count += len(arrLeft) - i  # Counting inversions
        k += 1

    while i < len(arrLeft):
        arr[k] = arrLeft[i]
        k += 1
        i += 1

    while j < len(arrRight):
        arr[k] = arrRight[j]
        k += 1
        j += 1

# Example usage:
arr = [5, 3, 8, 6, 4, 1]
mergeSort(arr)
print("Sorted Array:", arr)
print("Number of Inversions:", inversions_count)
