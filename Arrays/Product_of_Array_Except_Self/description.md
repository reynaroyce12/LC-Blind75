## [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)

**Problem Description:**  
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

**Difficulty:** `Medium`  
**Category:** `Array`, `Prefix Product`, `Suffix Product`

**Example Input/Output:**  
**Input:** `nums = [1,2,3,4]`  
**Output:** `[24,12,8,6]`  
**Explanation:**  
- The product of elements except for `nums[0]` = `2*3*4 = 24`.  
- The product of elements except for `nums[1]` = `1*3*4 = 12`.  
- The product of elements except for `nums[2]` = `1*2*4 = 8`.  
- The product of elements except for `nums[3]` = `1*2*3 = 6`.  

---

### Solution: Prefix and Suffix Product Approach  


1. **Left product:** As we go through the array, we calculate the product of all elements to the left of each index and store it.

2. **Right product:** As we go through the array in reverse, we calculate the product of all elements to the right of each index and multiply it with the stored left product.

By using two variables, `left_prod` and `right_prod`, we efficiently keep track of these calculations in one forward pass and one backward pass through the array.

*Time Complexity:* `O(n)` – We traverse the array twice (forward and backward).  
*Space Complexity:* `O(1)` – We use the output array `answer` for computation without allocating extra space.
