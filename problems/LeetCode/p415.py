class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ind = len(num1) if len(num1) < len(num2) else len(num2)
        p = 1
        su = 0
        while p <= ind:
            su += (int(num1[-p]) + int(num2[-p])) * (10 ** (p-1))
            p += 1

        while p <= len(num1):
            su += int(num1[-p]) * (10 ** (p-1))
            p += 1

        while p <= len(num2):
            su += int(num2[-p]) * (10 ** (p-1))
            p += 1

        return str(su)

    def addStrings2(self, num1: str, num2: str) -> str:
        ind = len(num1) if len(num1) < len(num2) else len(num2)
        p = 1
        su = ""
        while p <= ind:
            su += (int(num1[-p]) + int(num2[-p]))
            p += 1

        while p <= len(num1):
            su += num1[-p]
            p += 1

        while p <= len(num2):
            su += num2[-p]
            p += 1

        return su[::-1]




print(Solution().addStrings( "11", "123"))