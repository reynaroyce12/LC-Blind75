from collections import Counter

# Approach 1. Using Dictionary
class Solution_1(object):
    def isAnagram(self, s, t):

        if len(s) != len(t):
            return False

        s_frequency = {}
        t_frequency = {}

        for char in s:
            s_frequency[char] = s_frequency.get(char, 0) + 1

        for char in t:
            t_frequency[char] = t_frequency.get(char, 0) + 1

        return s_frequency == t_frequency


# Approach 2. Using Counter method from collections package
class Solution_2(object):
    def isAnagram(self, s, t):
        return Counter(s) == Counter(t)
