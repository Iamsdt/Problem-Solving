from typing import List


class Solution:
    def findRightInterval2(self, intervals: List[List[int]]) -> List[int]:
        res = []

        for i, value in enumerate(intervals):
            index = -1
            m_value = float('inf')
            for jj in range(0, len(intervals)):
                if jj == i:
                    continue

                if intervals[jj][0] >= value[1]:
                    if intervals[jj][0] < m_value:
                        m_value = intervals[jj][1]
                        index = jj

            res.append(index)

        return res

    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        res = []

        si = [(intervals[i][0], i) for i in range(len(intervals))]

        # now sort this
        si.sort(key=lambda x: x[0])

        for i, value in enumerate(intervals):
            # run binary search
            a, b = 0, len(si)
            # allow to run the search
            # The code checks if the start
            # value of the interval at
            # the midpoint si[m][0] is greater than
            # or equal to the ending value of the current interval value[1].
            # If true, it means we have found a potential right interval.
            # In that case, the upper bound b is updated to m,
            # as we continue searching for a potentially smaller right interval.
            while a < b:
                m = (a + b) // 2
                if si[m][0] >= value[1]:
                    b = m
                else:
                    a = m + 1

            # if is inside the array
            # then we found it else -1
            if a < len(si):
                index = si[a][1]
            else:
                index = -1

            res.append(index)

        return res


if __name__ == '__main__':
    print(Solution().findRightInterval2([[3, 4], [2, 3], [1, 2]]))
    print(Solution().findRightInterval2([[1, 4], [2, 3], [3, 4]]))
