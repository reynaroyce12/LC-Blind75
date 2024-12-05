## Missing Number

Problem Description: Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array

Difficulty: `Easy`

**Example Input/Output:**  
**Input:** [3, 0, 1]  
**Output:** 2  
**Explanation:** The missing number in the range [0, 1, 2, 3] is 2.

## Solution 1. Using Sets

Using this approach, we first initialise a set from the given array and then we iterate from 0 to the length of the array + 1. This is dont to handle the edge cases where:

1. If the missing number is 0: If the array starts from 1 and the missing number is 0, it will be correctly identified because we are iterating from 0.  
2. If the missing number is n: Since we iterate up to len(nums), the missing number could be n. If we dont iterate till n, we could overlook this edge case.    

*Time Complexity:* O(n)  
*Space Complexity:* O(n)

## Solution 1. Using Expected vs Actual Sum 

`Optimal Solution`  
In this technique, we use the mathematical formula to find the sum of n natural number which is n * (n+1) / 2. This will be the expected sum. We then subtract the actual sum of the elements in the array using the built-in function `sum` from the expected sum. The difference will be the missing number in the array

*Time Complexity:* O(n) because the sum function needs to iterate through all n elements of the array.  
*Space Complexity:* O(1)