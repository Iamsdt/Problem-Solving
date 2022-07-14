"""
Like Merge Sort, QuickSort is a Divide and Conquer algorithm.
It picks an element as a pivot and partitions the given array around the picked pivot.
 There are many different versions of quickSort that pick pivot in different ways.

Always pick the first element as a pivot.
Always pick the last element as a pivot (implemented below)
Pick a random element as a pivot.
Pick median as the pivot.

Ways (simplified):
•    take pivot from last (my version)
•    now find appropriate position in array
keep track of ith position, when iteration done, pivot position will be i+1 th
(if current element is less than pivot then swap with i position)
now back the arr on new pivot position and run again


Complexity: (Time Space trade off)
- Time: O(n2)
- Space: O(1)
"""


def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
            print(arr, pivot, j, i, arr[i])
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quickSort(arr, low=0, high=None):
    if not high:
        high = len(arr) - 1

    if low < high:
        pivotPos = partition(arr, low, high)
        quickSort(arr, low, pivotPos - 1)
        quickSort(arr, pivotPos + 1, high)


if __name__ == "__main__":
    arr = [2, 5, 1, 4, 3]
    quickSort(arr)
    print(arr)
