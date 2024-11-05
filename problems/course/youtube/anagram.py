from collections import Counter

def isAnagram(s1, s2):
    if len(s1) != len(s2):
        return False

    feq = {}
    feq2 = {}

    for ch in s1:
        feq[ch] = feq[ch] + 1 if ch in feq else 1

    for ch in s2:
        feq2[ch] = feq2[ch] + 1 if ch in feq2 else 1

    for key in feq:
        if key not in feq2 or feq[key] != feq2[key]:
            return False

    return True


def isAnagramPythonIC(s1, s2):
    return Counter(s1) == Counter(s2)


def isAnagramPythonIC(s1, s2):
    # sorted complexity logN, so total nlogN
    return sorted(s1) == sorted(s2)