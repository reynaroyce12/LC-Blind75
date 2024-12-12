class Solution(object):
    def containsDuplicate(self, n):
        return len(n) != len(set(n))

solution = Solution()
n = [1,2,3,4,1]
result = solution.containsDuplicate(n)
print(result)

