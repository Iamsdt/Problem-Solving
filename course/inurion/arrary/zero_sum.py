# Problem 1 and Problem2
# Problem 1: check any subarray which sum is zero
# Problem 2: check all the possible subarray which sum are zero

# problem statements
# [1, 2, 3, 5, -3, -5] find which subarray sum is zero
# subarray vs sub sequence
# subarray -> single elements or sequential numbers from array [3,5,-3]
# sub sequence -> any numbers [1, -5]

def solution(arr):
    """
        Naive approach,
        time complexity n*2
        space complexity 1
        """
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if sum(arr[i:j + 1]) == 0:
                return i, j
            j += 1

    return -1, -1


# lets improve
def solution2(arr):
    """
    Prefix sum approach,
    time complexity n
    space complexity n
    if we want to improve time complexity
    """
    di = {}
    prefix_sum = [0] * len(arr)
    for i, v in enumerate(arr):
        if i == 0:
            prefix_sum[i] = v
        else:
            prefix_sum[i] = v + prefix_sum[i - 1]

    print(prefix_sum)
    for i in range(len(prefix_sum)):
        v = prefix_sum[i]
        if v == 0:
            return 0, i
        if v in di:
            # return index
            return di[v] + 1, i
        else:
            di[v] = i

    return -1, -1


def print_info(arr, v):
    res = arr[v[0]] + arr[v[1]]
    print(f"Index: {v[0]}, {v[1]} -> sub array:{arr[v[0]:v[1] + 1]} which is {sum(arr[v[0]:v[1] + 1]) == 0}")


if __name__ == "__main__":
    arr = [4, -4, 8, 0, 4, -4]
    target = 35
    print("Naive Approach")
    v = solution(arr)
    print_info(arr, v)
    print("\nPrefix sum Approach")
    v = solution2(arr)
    print_info(arr, v)


# problem statements
# [1, 2, 3, 5, -3, -5] return all sub array, which sums are zero
# Answer:
# use prefix sum, then put in dict as array on index
# if length is more than 1, then there are some answer
# now use indices array and make all possible combination
# if key is zero, possible combination will be from 0 to value

def solution4(arr):
    di = {}
    prefix_sum = [0] * len(arr)
    for i, v in enumerate(arr):
        if i == 0:
            prefix_sum[i] = v
        else:
            prefix_sum[i] = v + prefix_sum[i - 1]

    print("Prefix sum", prefix_sum)
    for i in range(len(prefix_sum)):
        if prefix_sum[i] not in di:
            di[prefix_sum[i]] = [i]
        else:
            di[prefix_sum[i]].append(i)

    answer = []
    for key, value in di.items():
        if len(value) > 1 or key == 0:
            if key == 0:
                for val in value:
                    answer.append((0, val))

                for j in range(len(value)):
                    for k in range(j + 1, len(value)):
                        answer.append((value[j] + 1, value[k]))
            else:
                for j in range(len(value)):
                    for k in range(j + 1, len(value)):
                        answer.append((value[j] + 1, value[k]))

    return answer


if __name__ == "__main__":
    print("\n\nProblem 2")
    arr = [4, -4, 8, 0, 4, -4]
    target = 35
    v = solution4(arr)
    for i in v:
        print_info(arr, i)
