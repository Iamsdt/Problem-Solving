def twoNumberSum(array, targetSum):
    di = {}

    for i, v in enumerate(array):
        t = targetSum - v
        if t in di:
            return [array[di[t]], v]
        else:
            di[v] = i

    return []