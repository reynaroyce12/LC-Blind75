## [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

**Problem Description:**  
Suppose an array of length `n` sorted in ascending order is rotated between `1` and `n` times. For example, the array `nums = [0,1,2,4,5,6,7]` might become:

`[4,5,6,7,0,1,2]` if it was rotated `4` times.
`[0,1,2,4,5,6,7]` if it was rotated `7` times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array `nums` of unique elements, return the minimum element of this array.

You must write an algorithm that runs in `O(log n)` time.

**Difficulty:** `Medium`  
**Category:** `Array`, `Binary Search`

**Example Input/Output:**  
**Input:** [3, 4, 5, 1, 2]  
**Output:** 1  
**Explanation:**  
The array is rotated, and the minimum element is `1`.

---

## Solution. Using Binary Search

Since the requirement is to solve the problem in O(log n) time complexity, we can make use of the binary search algorithm. The property of the sorted array is that there will be two halves, the first half is sorted in increasing order, and the second half begins with a number smaller than the previous numbers, indicating the point of rotation. Our goal is to find this number. 

- Initialize two pointers, `left` and `right`. `left` will be initialised to 0 and `right` to `len(nums) - 1`

- While `left` is less than `right`, find the middle element `mid`.

- If `nums[mid] > nums[right]`, the minimum must be to the right of `mid`, so we update `left` to `mid + 1`.  

- Or if `nums[mid] <= nums[right]`, we set it as `right = mid`. This is because when a lesser number than `nums[right]` is found, there is a possibility that the lesser number itself will be the minimum number that we are looking for.

- Continue narrowing the search space until `left` equals `right`, at which point `nums[left]` will be the minimum.  


*Time Complexity:* (O(log n)): The binary search reduces the search space by half at each step, resulting in logarithmic time complexity.  

*Space Complexity:* (O(1)): We only use a constant amount of extra space, as we only need to store a few variables.
