from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        total = 0

        for values in grid:
            # now check last element
            # if last element gretter than zero
            # then continue
            if values[-1] > 0:
                continue

            # now run binarry search
            a, b = 0, len(values) - 1
            while a <= b:
                mid = (a+b)//2
                if values[mid] < 0:
                    total += len(values[mid:b+1])
                    b = mid - 1
                elif values[mid] >= 0:
                    a = mid + 1
        
        return total


if __name__ == "__main__":
    print(Solution().countNegatives(grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))
    print(Solution().countNegatives(grid = [[3,2],[1,0]]))