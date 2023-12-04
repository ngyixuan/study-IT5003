def bubbleSort(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr)-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def selectionSort(arr):
    for i in range(len(arr) - 1):
        # 记录最小数的索引
        minIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        # i 不是最小数时，将 i 和最小数进行交换
        if i != minIndex:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr

arr =[8,0,6,7,0,1,9 ]
# def insertionSort(arr):
#     for i in range(len(arr)):
#         preIndex = i-1
#         current = arr[i]
        
#         while preIndex >= 0 and arr[preIndex] > current:
#             arr[preIndex+1] = arr[preIndex]
#             preIndex-=1
#         arr[preIndex+1] = current
        
#     return arr

# print(insertionSort(arr))



def insertionSort(arr):
    for i in range(1,len(arr)):
        value = arr[i]
        hole = i
        while(hole>0 and arr[hole-1]>value):
            arr[hole] = arr[hole-1]
            hole = hole-1
        arr[hole] = value
    return arr


arr = [2,4,1,6,8,5,3,7]

def mergeSort(arr):
    if(len(arr)==1): return
    mid = len(arr)//2
    arrLeft = arr[:mid]
    arrRight = arr[mid:]
    print(arr,arrLeft,arrRight)
    mergeSort(arrLeft)
    mergeSort(arrRight)
    merge(arrLeft,arrRight,arr)

def merge(arrLeft,arrRight,arr):
    i,j,k=0,0,0
    # 把先把分解出来的子数组进行排序
    while(i<len(arrLeft) and j<len(arrRight)):
        if(arrLeft[i]<arrRight[j]):
            arr[k] = arrLeft[i]
            i+=1
        else:
            arr[k] = arrRight[j]
            j+=1
        k+=1
    # 如果左边还有剩下的还没放到arr中，就直接顺序排放

    while(i<len(arrLeft)): 
        arr[k] = arrLeft[i]
        k+=1
        i+=1
    # 如果右边还有剩下的还没放到arr中，就直接顺序排放
    
    while(j<len(arrRight)):
        arr[k] = arrRight[j]
        k+=1
        j+=1

    print("sorted",arr)

arr = [2,4,1,6,8,5,3,7]

def quickSort(arr):
    p_index = partition(arr)


def partition(arr,start,end):
    pivot = arr[end]
    
    for i in range(end):
        if(arr[i]<=pivot):
            arr[start],arr[i] = arr[i], arr[start]
            start +=1

    arr[start+1],arr[end] = arr[]


    