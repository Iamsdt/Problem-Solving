class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {'(': ')', '[': ']', '{': '}'}
        for c in s:
            if c in ['(', '[', '{']:
                stack.append(c)
            elif not stack or match[stack.pop()] != c:
                return False
        return not stack



if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.isValid("([)]{}"))