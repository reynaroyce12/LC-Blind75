class Solution(object):
    def maxSubArray(self, nums):
        current_sum = 0
        max_sum = float("-inf")

        for n in nums:
            if current_sum < 0:
                current_sum = 0
            current_sum += n
            max_sum = max(max_sum, current_sum)

        return max_sum

solution = Solution()
nums = [-9, 2, 1, 4, 5]
result = solution.maxSubArray(nums)
print(result)
