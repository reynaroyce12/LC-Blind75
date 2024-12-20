## [Two Sum](https://leetcode.com/problems/two-sum/)

**Problem Description:**  

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

**Difficulty:** `Easy`  
**Category:** `Array`, `Hash Table`

**Example Input/Output:**  
**Input:** `nums = [2, 7, 11, 15], target = 9`  
**Output:** `[0, 1]`  
**Explanation:** The numbers at indices 0 and 1 add up to the target: `2 + 7 = 9`.



### Solution. Hash Map

This method uses a hash map to store each number and its corresponding index as we iterate through the `nums` array. For each element `nums[i]`, we compute its complement `target - nums[i]` and check if it already exists in the hash map. If it does, that means we have already encountered a number that adds up to the `target` with `nums[i]`, and we return the indices of the two numbers. If it doesn’t exist in the hash map, we store the current number and its index in the map and continue the iteration.

*Time Complexity:* `O(n)` – We iterate through the array once.  
*Space Complexity:* `O(n)` – We use a hash map to store the numbers and their indices.

