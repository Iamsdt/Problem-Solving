from typing import List


class Solution:
    def generate_box(self, old, total):
        gen = total - 2
        if gen  == 0:
            return [1, 1]

        ans = []
        p = 0 
        while p < len(old):
            if p >= gen:
                break
            ans.append(old[p] + old[p + 1])
            p += 1

        return [1] + ans + [1]

    def generate(self, numRows: int) -> List[List[int]]:

        ans = [[1]]

        for i in range(2, numRows+1):
            ans.append(self.generate_box(ans[-1], i))

        return ans



if __name__ == '__main__':
    print(Solution().generate(30))