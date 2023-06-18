class Solution:
    def isValid(self, s: str) -> bool:
        data = []
        match = {"(": ")", "[": "]", "{": "}"}
        for i in s:
            if i == "(" or i == "[" or i == "{":
                data.append(i)
            elif not data or match[data.pop()] != i:
                return False

        return not data


if __name__ == '__main__':
    print(Solution().isValid("()"))
