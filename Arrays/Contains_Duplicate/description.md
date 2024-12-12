## Contains Duplicate

**Problem Description:**  
Given an integer array `n`, determine if any value appears at least twice in the array. If any value is repeated, return true; otherwise, return false.

**Difficulty:** `Easy`  
**Category:** `Array-based`


**Example Input/Output:**  
**Input:** [1, 2, 3, 4, 1]  
**Output:** true  
**Explanation:**  
The number `1` appears twice in the array, so the output is `true`.

---

## Solution. Using Set

**Explanation:**  
This approach leverages the properties of a set, which cannot contain duplicate elements.  

Steps:  
- Convert the input array `n` into a set.  
- Compare the length of the original array with the length of the set.  
- If the lengths are different, it means the array contains duplicate elements, and we return `true`.  
- If the lengths are the same, the array has no duplicates, and we return `false`.  

This method is simple and efficient for detecting duplicates in an array.

*Time Complexity:* \(O(n)\): Creating a set from the array takes \(O(n)\), where \(n\) is the length of the array.  
*Space Complexity:* \(O(n)\): The set requires additional space proportional to the size of the array.
