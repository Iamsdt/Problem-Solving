# Linear Search
def validAnagram(arr, t):
    start = -1
    end = -1
    for idx, v in enumerate(arr):
        if (v!=t):
            continue
        
        if start == -1:
            start = idx
        else:
            end = idx

    return [start, end]

def find_start(arr, t):
    if arr[0] == t: return 0

    low = 0
    high = len(arr) -1 
    mid = 0
    while high >= low:
        mid = (high + low) // 2
        if arr[mid] > t:
            high = mid - 1
        elif arr[mid] < t:
            low = mid + 1
        elif arr[mid] == t:
            return mid

    return -1


def validAnagramBinary(arr, t):
    start = find_start(arr, t)
    if start == -1 or arr[start] != t:
        return [-1, -1]

    end = -1
    
    for i in range(start, len(arr)):
        if arr[i] != t:
            break
        end = i

    return [start, end]




print(validAnagram([2, 3, 4, 5, 5, 5, 6, 7],5))
print(validAnagramBinary([2, 3, 4, 5, 5, 5, 6, 7],5))
print(validAnagram([5, 5, 5,5, 5, 5,5, 5, 5,5, 5, 5],5))
print(validAnagramBinary([5, 5, 5,5, 5, 5,5, 5, 5,5, 5, 5],5))
