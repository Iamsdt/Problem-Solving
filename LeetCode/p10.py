# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:

#         def check(i, j):
#             if i >= len(s) and j >= len(p):
#                 return True
            
#             if j >= len(p):
#                 return False

#             match = i < len(s) and (s[i] ==p[j] or p[j]=='.')
#             if (j+1) < len(p) and p[j+1] == "*":
#                 return (check(i, j+2) or (match) and check(i+1, j))

#             if match:
#                 return check(i+1, j+1)

#             return False

#         return check(0, 0)

#         # if p == s:
#         #     return True

#         # if len(p) == 0:
#         #     return True

#         # i = 0 # for s
#         # j = 0 # p

#         # if "*" not in p:
#         #     if "." in p:
#         #         while j < len(p):
#         #             if p[j] != p[j]:
#         #                return False 

#         #         return True
#         #     else:
#         #         return p == s
        
#         # while j < len(p):
#         #     if i >= len(s):
#         #         break
#         #     temp = p[j:]
            
#         #     if len(temp) == 0:
#         #         break

#         #     if "*" not in temp:
#         #         if p[j] == s[i]:
#         #             i += 1
#         #         else:
#         #             j += 1
#         #         continue

#         #     m = temp.split("*")[0]

#         #     if m == ".":
#         #         i+=1
#         #     elif p[j:j+len(m)] == s[i:i+len(m)]:
#         #         i += len(m)
#         #     else:
#         #         j += len(m) + 1

#         # return i == len(s)
        
class Solution(object):
    def isMatch(self, text, pattern):
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'}
        print("first_match", first_match)

        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or
                    first_match and self.isMatch(text[1:], pattern))
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])
        
if __name__ == "__main__":
   sol = Solution()
#    "mississippi"
# "mis*is*p*."

   print(sol.isMatch(text="aaa", pattern="a"))
#    print(sol.isMatch(text="aaa", pattern="a*"))
#    print(sol.isMatch(text="aaa", pattern=".*"))
   print(sol.isMatch(text="aab", pattern="c*a*b"))
#    print(sol.isMatch(text="mississippi", pattern="mis*is*p*."))

