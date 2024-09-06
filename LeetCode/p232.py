# Copyright (c) 2022 Shudipto Trafder
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []
        self.head = []

    def push(self, x: int) -> None:
        if not self.s1:
            self.head = x
        self.s1.append(x)

    def pop(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())

        return self.s2.pop()

    def peek(self) -> int:
        if self.s2:
            return self.s2[-1]

        return self.head

    def empty(self) -> bool:
        return not self.s1 and not self.s2