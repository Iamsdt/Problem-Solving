# FREE https://www.lintcode.com/problem/659/

# 4#lint4#code4#love3#you
# ['lint', 'code', 'love', 'you']

class Solution:
    def encode(self, strs):
        res = ""
        for i in strs:
            res += str(len(i)) + "#" + i
        return res

    def decode(self, str):
        res = []
        p = 0
        while p < len(str):
            j = p
            while str[j] != "#":
                j += 1

            length = int(str[p:j])
            res.append(str[j+1:j+1+length])

            p = j + 1 + length

        return res


if __name__ == '__main__':
    data = ["lint", "code", "love", "you"]
    encode = Solution().encode(data)
    print(encode)
    decode = Solution().decode(encode)
    print(decode)
