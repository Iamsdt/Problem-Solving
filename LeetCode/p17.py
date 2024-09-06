from itertools import combinations
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        di = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "qxyz"
        } 
        arr = ""
        for i in digits:
            arr += (di[int(i)])

        return list(combinations(arr, 1))



if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.letterCombinations("23"))