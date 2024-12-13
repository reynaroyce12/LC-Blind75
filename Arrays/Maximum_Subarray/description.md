# [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)

**Problem Description:**  
Given an integer array nums, find the subarray with the largest sum, and return its sum.

**Difficulty:** `Easy`   
**Category:** `Array`, `Dynamic Programming`, `Kadane's Algoritm`

**Example Input/Output:**  
**Input:** `nums = [-2,1,-3,4,-1,2,1,-5,4]`  
**Output:** `6`  
**Explanation:** The subarray `[4,-1,2,1]` has the largest sum = `6`.  

---

### Solution 1: Kadane's Algorithm  

This approach uses a greedy algorithm to find the maximum subarray sum. We iterate through the array while maintaining two variables:
- `current_sum`: the sum of the current subarray
- `max_sum`: the maximum sum found so far

At each step, we update `current_sum` by adding the current element to it. If `current_sum` becomes negative, we reset it to 0, since starting a new subarray at the next element is more beneficial. This is because the current subarray sum has become less than 0. Including this negative sum in subsequent subarrays would not be beneficial when we are trying to find a larger sum. In other words, a negative current_sum would decrease the total sum of any subsequent subarray.And finally if `current_sum` becomes greater than `max_sum`, we update it

*Time Complexity:* `O(n)` – We iterate through the array once.  
*Space Complexity:* `O(1)` – Only a few extra variables are used for the computation.


*Time Complexity:* O(n) – We iterate through the array once.  
*Space Complexity:* O(1) – Only a few extra variables are used for the computation.
