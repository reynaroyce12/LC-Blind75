## [Three Sum](https://leetcode.com/problems/3sum/)

**Problem Description:**  

Given an integer array `nums`, return all the unique triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, where `nums[i] + nums[j] + nums[k] == 0`.

Note that the solution set must not contain duplicate triplets.

**Difficulty:** `Medium`  
**Category:** `Array`, `Sorting`

**Example Input/Output:**  
**Input:** `nums = [-1, 0, 1, 2, -1, -4]`  
**Output:** `[[-1, -1, 2], [-1, 0, 1]]`  
**Explanation:**  
The triplets that sum to zero are:
- `[-1, -1, 2]`
- `[-1, 0, 1]`

### Solution: Two Pointer Approach

This method uses the **two-pointer technique** on a sorted array to  find valid triplets. The steps are as below:

1. **Sort the Array**: Begin by sorting the input array. Sorting helps in two ways: it allows us to easily avoid duplicates, and it also enables efficient search using the two-pointer approach.
  
2. **Iterate Through the Array**: Use an index `i` to iterate over the array. For each `i`, consider it as the first element of the triplet. The condition `for i in range(len(nums) - 2):` ensures that we stop when there are fewer than three elements left to form a triplet.

3. **Two Pointers Setup**: Set two pointers:
   - `left` initialized to the next element after `i` (i.e., `i + 1`).
   - `right` initialized to the last index of the array.
   
4. **Check the Sum**: For each pair of elements (`sorted_nums[left]`, `sorted_nums[right]`):
   - If `sorted_nums[i] + sorted_nums[left] + sorted_nums[right] == 0`, a valid triplet is found. Add this triplet to the resultant array.
   - If the sum is less than 0, increment `left` by 1 to increase the sum (since the array is sorted).
   - If the sum is greater than 0, decrement `right` by 1 to decrease the sum.

5. **Skip Duplicates**: To avoid counting duplicate triplets, skip over elements that have already been checked. This can be done by checking if the current number is the same as the previous one.

*Time Complexity:* `O(n^2)` – Sorting takes `O(n log n)`, and the two-pointer traversal for each element takes `O(n)`.  
*Space Complexity:* `O(1)` – We only use a constant amount of extra space (ignoring the input array).
