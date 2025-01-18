class Solution(object):
    def longestPalindrome(self, s):

        longest_palindrome = ""

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left = left - 1
                right = right +1
            return s[left + 1 : right]
        
        for i in range(len(s)):
            odd_palindrome = expand(i, i)
            even_palindrome = expand(i, i + 1)

            longest_palindrome = max(longest_palindrome, odd_palindrome, even_palindrome, key=len)
            

        return longest_palindrome

