class Solution:
    def reverseVowels(self, s: str) -> str:
        p, q = 0, len(s)-1
        data = list(s)
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        while p <= q:
            if data[p] in vowels and data[q] in vowels:
                data[p], data[q] = data[q], data[p]            
            elif data[p] in vowels:
                q -= 1
                continue
            elif data[q] in vowels:
                p += 1
                continue
            
            p += 1
            q -= 1

        return "".join(data)


if __name__ ==  '__main__':
    print(Solution().reverseVowels("Euston saw I was not Sue."))
    print(Solution().reverseVowels2("Euston saw I was not Sue."))
