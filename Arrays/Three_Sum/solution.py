class Solution(object):
    def threeSum(self, nums):
        resultant_array = []
        sorted_nums = sorted(nums)

        for i in range(len(sorted_nums) - 2):
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue

            left = i + 1
            right = len(sorted_nums) - 1

            while left < right:
                total = sorted_nums[i] + sorted_nums[left] + sorted_nums[right]

                if total == 0:
                    resultant_array.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])

                    while left < right and sorted_nums[left] == sorted_nums[left + 1]:
                        left = left + 1
                    while left < right and sorted_nums[right] == sorted_nums[right - 1]:
                        right = right - 1
                    
                    left = left + 1
                    right = right - 1
                elif total < 0:
                    left = left + 1
                elif total > 0:
                    right = right -1
                
        return resultant_array

