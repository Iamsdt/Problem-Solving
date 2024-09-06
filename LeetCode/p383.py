class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in ransomNote:
            if i not in magazine:
                return True

            magazine = magazine.replace(i, "", 1)



# for i in ransomNote:
# 	        if i in magazine:
#                 magazine = magazine.replace(i, "", 1)
#             else:
# 				return False
            
# 		return True