from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in operations:
            if i == "C":
                stack.pop()
            elif i == "D":
                a = stack[-1]*2
                stack.append(a)
            elif i == "+":
                s= stack[-1]+stack[-2]
                stack.append(s)
            else:
                stack.append(int(i))


        return sum(stack)

if __name__ == '__main__':
    print(Solution().calPoints(["5","2","C","D","+"]))