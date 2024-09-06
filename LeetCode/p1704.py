from collections import Counter

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        w1, w2 = 0, 0
        t='aieouAEIOU'
        for i in range(len(s)//2):
            if s[i] in t: 
                w1+=1
            if s[-i-1] in t:
                w2+=1
        return True if w1==w2 else False




if __name__ ==  '__main__':
    print(Solution().halvesAreAlike("book"))
    # print(Solution().halvesAreAlike("textbook"))