from collections import Counter
from typing import List

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        # Create Hashmap to maintain count of words
        lookup = Counter(words)
        
        # Result Variable
        p_len = 0
        mid = 0
        
        # Iterating over the hashmap keys
        for word in lookup.keys():
            
            # If word is like 'aa', 'bb' then follow this steps
            if word[0] == word[1]:
                
                # Suppose if count of 'aa' is 2 then we will take all the 4 words
                # As 'aa' + 'aa' is palindrome
                if lookup[word]%2 == 0:
                    p_len += lookup[word]
                else:
                    # Suppose if count of 'aa' is 3 then we can take all the 3 word
                    # As 'aa' + 'aa' + 'aa' is also palindrome 
                    p_len += lookup[word]-1
                    mid = 1
                    
            elif word[::-1] in lookup:
                # If reverse of word is present in hashmap
                # then we can create palindrome using current and reverse word
                p_len += min(lookup[word], lookup[word[::-1]])
        
        # Return the result by multiplying it by 2
        # As we are only maintaing the count of words
        # Every word lenght is 2
        return (p_len + mid) * 2