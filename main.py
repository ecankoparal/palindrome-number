class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False
        
        reversed = 0
        temp = x

        while temp > 0:            
            lastDigit = temp % 10
            reversed = reversed * 10 + lastDigit

            temp = temp // 10
        
        return reversed == x
