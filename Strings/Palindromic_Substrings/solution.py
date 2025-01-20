class Solution(object):
    def countSubstrings(self, s):
        valid_palindromes = 0

        def expand(left, right):
            nonlocal valid_palindromes
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    valid_palindromes += 1
                    left -= 1
                    right += 1
                else:
                    break

        for i in range(len(s)):
            expand(i, i) # For odd length palindrome
            expand(i, i + 1) # For even length palindrome

        return valid_palindromes


