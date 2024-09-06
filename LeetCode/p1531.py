
from collections import Counter, OrderedDict

class Solution(object):
    # def getLengthOfOptimalCompression1(self, s, k):
    #     """
    #     :type s: str
    #     :type k: int
    #     :rtype: int
    #     """
    #     di = {}
    #     for i in s:
    #         if i in di:
    #             di[i] += 1
    #         else:
    #             di[i] = 1

    #     # now 
    #     print(di)
    #     li = []
    #     for i in di.keys():
    #         li.append((i, di[i]))
        
    #     # now sort based on value
    #     li.sort(key=lambda x: x[1])
        
    #     for i in li:
    #         key, value = i
    #         if k <= 0:
    #             break
    #         if value > k:
    #             di[key] = value - k
    #             k = 0
    #         else:
    #             di[key] = 0
    #             k -= value

    #     ans = ""
    #     print(di)
    #     for i in di.keys():
    #         value = di[i]
    #         if value == 0:
    #             continue

    #         ans += i+str(value) if value > 1 else i

    #     return len(ans)

    # def getLengthOfOptimalCompression2(self, s, k):
    #     #di = Counter(s)
    #     # li = sorted(di.items(),key = lambda i: i[1])
    #     # if k == 0:
    #     #     new_str = "".join([key+str(value) if value > 1 else key for key, value in di.items()])
    #     #     return len(new_str)
    #     # new_str = "".join([key*value if value > 1 else key for key, value in li])
    #     # print("New string: " + new_str)

    #     cache = {}
    #     new_str = s
    #     ans = float('inf')

    #     def check_minimum(ans, pos):
    #         if pos > len(new_str):
    #             return ans

    #         temp_s = new_str[0:pos]+new_str[pos+k:]
    #         # print("Temp", temp_s)
    #         temp_k = k
    #         if temp_s in cache:
    #             return cache[temp_s]

    #         di = Counter(temp_s)
    #         row_min = float('inf')
    #         if k == 0:
    #             v = "".join([key+str(value) if value > 1 else key for key, value in di.items()])
    #             return len(v)
    #         for key, value in di.items():
    #             if temp_k <= 0:
    #                 break
    #             if value > temp_k:
    #                 di[key] = value - temp_k
    #                 temp_k = 0
    #             else:
    #                 di[key] = 0
    #                 temp_k -= value

    #         final_str = "".join([key+str(value) if value > 1 else key for key, value in di.items()])
    #         # print(final_str)
    #         row_min = min(row_min, len(final_str))
    #         current = check_minimum(row_min, pos+k)
    #         return min(ans, current)
            
    #     return check_minimum(ans, 0)

    # solved by @xu_tony
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        def helper(s, cur, last, count, k, dp):
            print(cur, last, count, k)
            if k < 0:
                return float('inf')
            # base case, running the full length of s
            if cur >= len(s):
                return 0

            # if already memorized, reduce the complexity and directly return
            if (cur, last, count, k) in dp:
                return dp[(cur, last, count, k)]

            result = float('inf')
            # delete one char
            result = helper(s, cur + 1, last, count, k - 1, dp)
            print("First call results", result)
            # construct the string
            if s[cur] != last:
                # if not the same as the previous char
                print("********** IF not match *********")
                res1 = helper(s, cur + 1, s[cur], 1, k, dp)
                print("Again call", res1, result)
                result = min(result, 1 + res1)
                print("Final Res", result)
                print("********** IF not match *********")
            else:
                # the same as the previous char
                # if the 2nd char (a->a2) and 10th char(a9->a10) and 100th char(a99->a100),
                # we need to add one more char.
                if count == 1 or count == 9 or count == 99:
                    result = min(result, 1 + helper(s, cur + 1, last, count + 1, k, dp))
                    print("If 1, 99", result)
                else:
                    # otherwise, concat the current char.
                    result = min(result, helper(s, cur + 1, last, count + 1, k, dp))
                    print("match results", result)

            # memorize
            dp[(cur, last, count, k)] = result
            return result

        return helper(s, 0, '', 0, k, {})




if __name__ == '__main__':
    s = Solution()
    # print(s.getLengthOfOptimalCompression("aaabcccd", 2))
    # print(s.getLengthOfOptimalCompression2("aabbaa", 2))
    # print(s.getLengthOfOptimalCompression2("aaaaaaaaaaa", 0))
    # print(s.getLengthOfOptimalCompression2("llllllllllttttttttt", 1))
    print(s.getLengthOfOptimalCompression("abc", 2))
    # print(s.getLengthOfOptimalCompression("bababbaba", 1))
    # "bababbaba" 1