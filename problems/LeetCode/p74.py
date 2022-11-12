from typing import List


class Solution:
    def binarySearch(self, li, t):
        if li[0] == t: return True

        p = 0
        q = len(li) - 1

        while p <= q:
            mid = (p + q) // 2
            if li[mid] < t:
                p = mid + 1
            elif li[mid] > t:
                q = mid - 1

            else:
                return True

        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        col = len(matrix[0])

        p, q = 0, rows-1
        while p <= q:
            mid = (p + q) // 2
            print(matrix[mid], target, matrix[mid][-1])
            if matrix[mid][-1] < target:
                p = mid + 1
            elif matrix[mid][0] > target:
                q = mid - 1
            else:
                break

        print(p, q)
        if not (p <= q):
            return False


        mid = (p + q) // 2
        row = matrix[mid]
        print(row)

        # TIME: nlogn
        # for i in matrix:
        #     u = i[0]
        #     l = i[-1]
        #     if u <= target <= l:
        #         return self.binarySearch(i, target)

        return self.binarySearch(row, target)



if __name__ == '__main__':
    print(Solution().searchMatrix(matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]], target= 20))