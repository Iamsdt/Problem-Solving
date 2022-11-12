class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ""

        # handle 1000
        if num >= 1000:
            v = num//1000
            ans += "M" * v
            num -= 1000 * v

        # handle second
        if num >= 100:
            v = num//100
            if v <= 9 and v > 5:
                ans += "CM" if v == 9 else "D" + "C" * (v-5)
                num -= 100 * v
            elif v == 4:
                ans += "CD"
                num -= 100 * v
            else:
                ans += "C" * v
                num -= 100 * v

        # handle last one
        if num > 10:
            v = num//10
            if v <= 9 and v >= 5:
                ans += "XC" if v == 9 else "L" + "X" * (v-5)
                num -= 10 * v
            elif v == 4:
                ans += "XL"
                num -= 10 * 4
            else:
                ans += "X" * v
                num -= 10 * v

        if num >= 9 and num >=5:
            ans += "IX" if v == 9 else "V" + "I"*(num-5)
        elif num == 4:
            ans += "IV"
        else:
            ans += "I" * num

        return ans


if __name__ == '__main__':
    li = [3, 58, 3344, 20]
    for i in li:
        print(Solution().intToRoman(i))