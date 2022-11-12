class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0

        # check sign first
        sign = True
        if s[0] in ["+", "-"]:
            sign = True if s[0] == "+" else False
            s = s[1:]

        
        value = 0
        for ch in s:

            # check this is string
            if not ch.isdigit():
                break

            v = value * (10)
            value = v + int(ch)
                

        # now convert
        num =  value if sign else -value
        if num < -2**31:
            return -2**31
        elif num > (2**31 -1):
            return 2**31 -1

        return num



if __name__ == '__main__':
    li = ["42", "   -42", "4193 with words", "-91283472332", "3.14159"]
    for i in li:
        print(Solution().myAtoi(i))