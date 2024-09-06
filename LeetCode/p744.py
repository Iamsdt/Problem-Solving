from typing import List




# working but hard way
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if not letters:
            return letters
        
        p, q = 0, len(letters) - 1
                
        lowest = ""

        while p <= q:
            m = (p + q) // 2
            v = letters[m]
            
            if v <= target:
                p = m+1
            elif v > target:
                q = m-1
                # check lowest
                if not lowest:
                    lowest = letters[m]
                elif v < lowest:
                    lowest = letters[m]

        return lowest if lowest else letters[0]
    
    
# easy way
# def nextGreatestLetter(self, letters: List[str], target: str) -> str:
#         if not letters:
#             return letters
        
#         p, q = 0, len(letters) - 1
#         # check boundaries
#         if letters[p] < target < letters[q]:
#             return letters[q]
        
#         while p <= q:
#             m = (p + q) // 2
#             v = letters[m]
#             if v > target:
#                 q = m - 1
#             elif v <= target:
#                 p = m + 1
            
#         return letters[p]
    
    
if __name__ == "__main__":
    s = Solution()
    print(s.nextGreatestLetter(letters = ["c","f","j"], target = "a"))
    print(s.nextGreatestLetter(letters = ["c","f","j"], target = "c"))
