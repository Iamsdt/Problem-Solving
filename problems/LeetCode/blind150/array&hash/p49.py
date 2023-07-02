from collections import Counter
import collections
from typing import List

class Solution:
    # space n
    # space n * k
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:        
        # update
        di = collections.defaultdict(list)
        
        for i in strs: # n
            ana = tuple(sorted(i)) # k
            if ana in di:
                di[ana] = [i] + di[ana]
            else:
                di[ana] = [i]
                
        return di.values()
    
    
class Solution5:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)

        for s in strs:
            # generate a unique key
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        print(ans)
        return list(ans.values())
    
    
if __name__ == '__main__':
    print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    # print(Solution().groupAnagrams([""]))