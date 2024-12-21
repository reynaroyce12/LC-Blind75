## [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)

**Problem Description:**  
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, `nums` is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array `nums` after the possible rotation and an integer target, return the `index` of `target` if it is in nums, or -1 if it is not in nums.

You must solve it in `O(log n)` time complexity.

**Difficulty:** `Medium`  
**Category:** `Array`, `Binary Search`

---

**Example Input/Output:**  
**Input:** `nums = [4,5,6,7,0,1,2], target = 0`  
**Output:** `4`  
**Explanation:**  
The target `0` is located at index `4` in the array.  

**Input:** `nums = [1], target = 0`  
**Output:** `-1`  

---

### Solution. Modified Binary Search  


   The array is partially sorted due to the rotation. At any point during the binary search, one half of the array will always be sorted. This property can be used to decide which half to search next.  


   - Use two pointers, `left` and `right`, initialized to the start and end of the array, respectively.  
   - While `left <= right`, calculate the `mid` index.  
   - Compare `nums[mid]` with `target`:
     - If they are equal, return `mid`.  
     - Otherwise, determine which half of the array is sorted:
       - If the left half is sorted (`nums[left] <= nums[mid]`), check if `target` lies within this range. If yes, adjust `right`, otherwise adjust `left`.  
       - If the right half is sorted (`nums[mid] < nums[right]`), check if `target` lies within this range. If yes, adjust `left`, otherwise adjust `right`.  
   - If the loop ends without finding the target, return `-1`.  

*Time Complexity:* `O(log n)` – Binary search halves the search space at each step.  
*Space Complexity:* `O(1)` – No extra space is used.  
