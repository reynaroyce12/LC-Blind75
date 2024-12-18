## [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)

**Problem Description:**  
Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest product and return that product.

**Difficulty:** `Medium`  
**Category:** `Array`, `Dynamic Programming`

**Example Input/Output:**  
**Input:** [2, 3, -2, 4]  
**Output:** 6  
**Explanation:**  
The subarray [2, 3] has the largest product 6.




## Solution. Using Programming Approach

This method maintains two variables, `current_max` and `current_min`, to track the maximum and minimum products of the subarray at each position in the array. This is necessary because negative numbers can turn the minimum product into the maximum when multiplied.  

- Initialize `current_max`, `current_min`, and `result` as the first element in the array.  
- Iterate through the array from the second element, updating `current_max` and `current_min` by considering three possibilities for each number:
  - The number itself (`num`),  
  - The product of the previous maximum and the current number (`current_max * num`),  
  - The product of the previous minimum and the current number (`current_min * num`).
- Update the result to keep track of the highest product encountered so far.  
- Finally, return the `result` as the largest product.

*Time Complexity:* \(O(n)\): We iterate through the array once, so the time complexity is linear, where \(n\) is the length of the array.  
*Space Complexity:* \(O(1)\): We use a constant amount of extra space, as we only need to store a few variables.
