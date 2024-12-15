# Approach 1. Using Reversed String
class Solution_1(object):
    def isPalindrome(self, s):

        alpha_numeric_s = "".join(char for char in s if char.isalnum()).lower()
        reversed_string = alpha_numeric_s[::-1]
        
        if alpha_numeric_s == reversed_string:
            return True
        else:
            return False
            

# Approach 2. Using Two Pointers
class Solution_2(object):
    def isPalindrome(self, s):

        left = 0
        right = len(s) - 1

        while left < right:

            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True




