from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {
            "+": lambda x, y: x+y,
            "-": lambda x, y: x-y,
            "*": lambda x, y: x*y,
            "/": lambda x, y: x/y,
        }

        for i in tokens:
            if i not in operations:
                stack.append(i)
                continue

            y = stack.pop()
            x = stack.pop()

            res = operations[i](int(x), int(y))
            stack.append(res)


        return int(stack.pop())