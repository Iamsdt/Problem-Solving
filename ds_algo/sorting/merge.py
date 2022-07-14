import random

"""
The Merge Sort algorithm is a sorting algorithm that is considered 
as an example of the divide and conquer strategy. 
So, in this algorithm, the array is initially divided into two equal
halves and then they are combined in a sorted manner. 
We can think of it as a recursive algorithm that continuously splits 
the array in half until it cannot be further divided. 
This means that if the array becomes empty or has only one element left,
the dividing will stop, i.e. it is the base case to stop the recursion. 
If the array has multiple elements, we split the array into halves and recursively
invoke the merge sort on each of the halves. Finally, when both the halves are sorted,
the merge operation is applied. Merge operation is the process of taking two smaller 
sorted arrays and combining them to eventually make a larger one.

Ways (simplified):
•    Declare left variable to 0 and right variable to n-1 
•    Find mid by medium formula. mid = (left+right)/2
•    Call merge sort on (left,mid)
•    Call merge sort on (mid+1,rear)
•    Continue till left is less than right
•    Then call merge function to perform merge sort.

Complexity: (Time Space trade off)
- Time: O(nlogn)
- Space: O(n)
"""


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


def merge(arr):
    if len(arr) <= 1:
        return arr

    m = len(arr) // 2
    a = merge(arr[:m])
    b = merge(arr[m:])
    return merge_sorted_array(a, b)


if __name__ == "__main__":
    inp = [*range(20)]
    random.shuffle(inp)
    print(inp)
    out = merge(inp)
    print(out)
