class Solution:
    def interpret(self, command: str) -> str:
        di = {
            "G": "G",
            "()": "o",
            "(al)": "al"
        }

        p = 0

        res = ""

        while p < len(command):
            if command[p] == "G":
                res += "G"
                p += 1
                continue
            
            if command[p] == "(":
                if p+1 < len(command) and command[p+1] == ")":
                    res += "o"
                    p += 2
                    continue

                elif(p+2 < len(command) and command[p+1] == "a" and command[p+2] == "l"):
                    res += "al"
                    p += 3

            p += 1

        return res
                

a = Solution().interpret("(al)G(al)()()G")
print(a)
print(a == "alGalooG")