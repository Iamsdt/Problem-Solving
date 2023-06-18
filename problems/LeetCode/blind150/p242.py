from collections import Counter

class Solution:
    # Time - O(n)
    # Space - O(n)
    def isAnagram(self, s: str, t: str) -> bool:
        # first check length
        if len(s) != len(t):
            return False
        
        ds = {}
        dt = {}
        for i in range(len(s)):
            vs = s[i]
            vt = t[i]
            ds[vs] = 1 + ds.get(vs, 0)
            dt[vt] = 1 + dt.get(vt, 0)
            
        # just compare
        # for i in ds.keys():
        #     # if ds key not available in dt key
        #     if i not in dt.keys():
        #         return False
        #     if ds[i] != dt[i]:
        #         return False
            
        # even python can compare dt and ds
        return ds == dt
    
    # Tricked solution
    def isAnagram2(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
    
    # use this for space (1), some times it considered that
    # sorting does not take any extra space
    # but it increase time complexity
    def isAnagram3(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    
    
if __name__ == '__main__':
    print(Solution().isAnagram(s = "anagram", t = "nagaram"))
    print(Solution().isAnagram(s = "rat", t = "car"))
    