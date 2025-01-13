class Solution(object):
    def containsDuplicate(self, n):
        return len(n) != len(set(n))


