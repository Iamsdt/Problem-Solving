class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        if len(set(palindrome)) == 1 and 'a' in set(palindrome):
            return palindrome[:-1]+'b'
        for index, each in enumerate(palindrome):
            if each != 'a':
                if index != len(palindrome)//2:
                    return palindrome[:index]+'a'+palindrome[index+1:]
                else:
                    return palindrome[:-1]+'b'
        return ""