from typing import List
    
    
class Solution:
    def compress(self, chars: List[str]) -> int:
        p, q = 0, 0
        while q < len(chars):
            # handle this case ["a","a","a","b","b","a","a"]
            chars[p] = chars[q]
            count = 1
            
            while q + 1 < len(chars) and chars[q] == chars[q+1]:
                q += 1
                count += 1
                
                
            if count > 1:
                for c in str(count):
                    chars[p+1] = c
                    p += 1
            
            q += 1
            p += 1
            
        
        return p
    
    
if __name__ == '__main__':
    inp = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    inp2 = ["a","a","a","b","b","a","a"]
    a = Solution().compress(inp2)
    print(inp[:a])