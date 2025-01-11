class Solution(object):
    def characterReplacement(self, s, k):
        left = 0
        char_count = {}
        max_frequency = 0
        max_length = 0

        for right in range(len(s)):
            if s[right] in char_count:
                char_count[s[right]] += 1
            else:
                char_count[s[right]] = 1

            window_size = (right - left) + 1
            max_frequency = max(max_frequency, char_count[s[right]])
            operation = window_size - max_frequency

            if operation <= k:
                max_length = max(max_length, window_size)
            else:
                char_count[s[left]] -= 1
                left += 1
            
        return max_length