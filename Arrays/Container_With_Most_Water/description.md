## [Container With Most Water](https://leetcode.com/problems/container-with-most-water/)

**Problem Description:**
You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the ith line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

**Difficulty:** `Medium`  
**Category:** `Array`, `Two Pointers`

**Example Input/Output:**  
**Input:** `height = [1,8,6,2,5,4,8,3,7]`  
**Output:** `49`  
**Explanation:** The maximum area of water the container can store is between lines at index 1 and index 8, where the height is 8 and the width is 7. The area is `8 * 7 = 49`.

### Solution: Using Two Pointers  

---

In this approach, we initialize two pointers: `left` pointing to the first element of the `height` array and `right` pointing to the last element. We then calculate the area formed by these two lines by multiplying the width (the distance between the `left` and `right` pointers) by the height (the minimum of the two lines). The reason we use the minimum height is that the amount of water a container can hold is limited by the shorter line. If the taller line is chosen, the shorter line will still be the limiting factor, and the water will spill over the shorter side. 

The pointers are moved based on the height of the lines. If `heights[left]` is greater than or equal to `heights[right]`, we keep the `left` pointer fixed and move the `right` pointer inward. Similarly, if `heights[right]` is greater than `heights[left]`, we move the `left` pointer inward. This strategy ensures that we always explore the possibility of a taller line, which could potentially increase the container's area.

This continues until the two pointers meet, making sure that all possible container sizes are considered.

*Time Complexity:* `O(n)` – We iterate through the array once, with the left and right pointers moving towards each other.  
*Space Complexity:* `O(1)` – We only use a constant amount of extra space for the two pointers and the `max_area` variable.