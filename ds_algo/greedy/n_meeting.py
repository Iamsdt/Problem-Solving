# Problem Statement:
# There is one meeting room in a firm.
# You are given two arrays, start and end each of size N. Return maximum meetings.
# Rule: say meeting start at 12, next meeting can start at 12

# Simple Explanation:
# 1. First merge two array into 2d array
# 2. sort based on end time
# now check if end time of current meeting is
# smaller than next meeting start time,
# use two pointer or
# for loop, take end time as -1


def meeting(start, end):
    arr = []
    for i in range(len(start)):
        arr.append([start[i], end[i]])

    # now sort array, here using bubble sort
    # because it's easy to implement
    # letter, will use quick sort
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            v = arr[j]
            w = arr[j + 1]
            if v[1] > w[1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    # here array is sorted
    meets = [arr[0]] if arr else []
    n = 1 if arr else 0
    p, q = 0, 1
    while q < len(arr):
        a = arr[p]
        b = arr[q]

        if a[1] < b[0]:
            meets.append(b)
            n += 1
            p += 1

        q += 1

    return n, meets


def meeting2(start, end):
    arr = []
    for i in range(len(start)):
        arr.append([start[i], end[i]])

    # we can use Timsort
    # Timsort is a hybrid sorting algorithm,
    # derived from merge sort and insertion sort,
    # designed to perform well on many kinds of real-world data
    # complexity -> nlogn
    arr.sort(key=lambda x: x[1])

    # here array is sorted
    meets = []
    n = 0
    last_time = -1
    for i in range(len(arr)):
        if last_time < arr[i][0]:
            n += 1
            last_time = arr[i][1]
            meets.append(arr[i])

    return n, meets


if __name__ == "__main__":
    s = [1, 3, 0, 5, 8, 5]
    e = [2, 4, 6, 7, 9, 9]

    m1, me1 = meeting(s, e)
    m2, me2 = meeting2(s, e)
    print(m1, m2, m1 == m2)
    print(me1)
    print(me2)

# Same as
# 1. activity selection problems
# 2. Job sequencing problems

# challenge
# 1. meet time should come with time also
# 2. between meeting there should be 15 min gap
