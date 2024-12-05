# Approach 1: Using sets
class Solution(object):
    def missingNumber(self, nums):
        nums_set = set(nums)

        for ele in range(0, len(nums) + 1):
            if ele not in nums_set:
                return ele

# Approach 2: Using Expected vs Actual Sum   
class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)

        return expected_sum - actual_sum




