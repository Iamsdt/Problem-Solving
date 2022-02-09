class Solution:
    def isPalindrome(self, x: int) -> bool:

        temp = x
        rev = 0

        while (temp > 0):
            dig = temp % 10
            rev = rev * 10 + dig
            # here we are reducing number by
            #  dividing number by 10
            temp //= 10 

        return x == rev

        # complexity: O(logN)