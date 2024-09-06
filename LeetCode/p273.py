class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        di = {
            1000000000: 'Billion', 1000000: 'Million', 1000: 'Thousand', 100: 'Hundred',
            90: 'Ninety', 80: 'Eighty', 70: 'Seventy', 60: 'Sixty', 50: 'Fifty', 40: 'Forty', 30: 'Thirty',
            20: 'Twenty',
            19: 'Nineteen', 18: 'Eighteen', 17: 'Seventeen', 16: 'Sixteen', 15: 'Fifteen', 14: 'Fourteen',
            13: 'Thirteen', 12: 'Twelve', 11: 'Eleven', 10: 'Ten',
            9: 'Nine', 8: 'Eight', 7: 'Seven', 6: 'Six', 5: 'Five', 4: 'Four', 3: 'Three', 2: 'Two', 1: 'One'
        }

        s = ""
        for key, value in di.items():
            v = num // key
            if not v:
                continue
            if key >= 100:
                s += self.numberToWords(v) + " "
            s += value + " "
            num = num % key

        return s.strip()


if __name__ == "__main__":
    print(Solution().numberToWords(543))
