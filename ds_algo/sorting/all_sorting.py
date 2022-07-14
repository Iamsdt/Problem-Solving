import copy
import random


##################################################
############## Buble Sort #######################
##################################################
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


##################################################
############## Insertion Sort ####################
##################################################

def insertion_sort(arr):
    for i in range(len(arr)):
        j = i - 1
        while j >= 0 and arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j -= 1


##################################################
############## Selection Sort ####################
##################################################
def selection_sort(arr):
    for i in range(len(arr)):
        fixed = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[fixed]:
                arr[fixed], arr[j] = arr[j], arr[fixed]


##################################################
############## Merge Sort ########################
##################################################
def merge_sorted_array(arr1, arr2):
    arr = []
    p, q = 0, 0

    while p < len(arr1) and q < len(arr2):
        if arr1[p] < arr2[q]:
            arr.append(arr1[p])
            p += 1
        else:
            arr.append(arr2[q])
            q += 1

    if p < len(arr1):
        for i in range(p, len(arr1)):
            arr.append(arr1[i])

    if q < len(arr2):
        for i in range(q, len(arr2)):
            arr.append(arr2[i])

    return arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    m = len(arr) // 2
    a = merge_sort(arr[:m])
    b = merge_sort(arr[m:])
    return merge_sorted_array(a, b)


##################################################
############## Quick Sort ########################
##################################################
def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quickSort(arr, low=0, high=None):
    if not high:
        high = len(arr) - 1

    if low < high:
        pivotPos = partition(arr, low, high)
        quickSort(arr, low, pivotPos - 1)
        quickSort(arr, pivotPos + 1, high)


##################################################
############## Quick Sort ########################
##################################################
def count_sort(arr):
    m = max(arr)
    count = [0] * (m + 1)

    for i in arr:
        count[i] += 1

    for i in range(1, m + 1):
        count[i] = count[i - 1] + count[i]

    sort = [0] * len(arr)

    for i in range(len(arr) - 1, -1, -1):
        sort[count[arr[i]] - 1] = arr[i]
        count[arr[i]] = count[arr[i]] - 1

    return sort


if __name__ == "__main__":
    inp = [*range(20)]
    random.shuffle(inp)
    print("Input:", inp)

    print("\n")
    bb = copy.deepcopy(inp)
    bubble_sort(bb)
    print("Bubble Sort", bb)

    print("\n")
    ins = copy.deepcopy(inp)
    insertion_sort(ins)
    print("Insertion Sort", ins)

    print("\n")
    sle = copy.deepcopy(inp)
    selection_sort(sle)
    print("Selection Sort", sle)

    print("\n")
    mr = copy.deepcopy(inp)
    mrp = merge_sort(mr)
    print("Merge Sort", mrp)

    print("\n")
    qr = copy.deepcopy(inp)
    quickSort(qr)
    print("Quick Sort", qr)

    print("\n")
    inp = [random.randint(0, 10) for _ in range(20)]
    print("Count sort inp:", inp)
    res = count_sort(inp)
    print("Count Sort:", res)
