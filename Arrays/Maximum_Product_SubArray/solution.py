class Solution(object):
    def maxProduct(self, nums):
        if not nums:
            return 0


        current_max = current_min = result = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            temp_max, temp_min = current_max, current_min
            current_max = max(num, temp_max * num, temp_min * num)
            current_min = min(num, temp_max * num, temp_min * num)

            result = max(result, current_max)
        return result

        