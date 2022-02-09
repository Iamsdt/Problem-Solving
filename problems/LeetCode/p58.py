class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # easy solution
        # return len(s.split()[-1])
        flag = False
        count = 0
        for x in s[::-1]:
            if x != " ":
                count += 1
                flag=True
                continue
            if flag == True:
                break
        
        return count


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.lengthOfLastWord("   fly me   to   the moon  "))