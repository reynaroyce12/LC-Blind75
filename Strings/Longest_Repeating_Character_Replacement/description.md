## (Longest Repeating Character Replacement)[https://leetcode.com/problems/longest-repeating-character-replacement/description/]

**Problem Description:**  
You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `k` times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

**Difficulty:** `Medium`  
**Category:** `Sliding Window`

**Example Input/Output:**  
**Input:** "AABABBA", k = 1  
**Output:** 4  
**Explanation:**  
We can change one 'B' to 'A' to get the substring "AAAA", which has a length of 4.



## Solution. Sliding Window Technique

Start with an empty window and expand it by moving the right pointer. For each step, calculate the number of operations required to make all characters in the window same.

It is calculated as window_size - max_frequency, where window_size is the current length of the window and max_frequency is the frequency of the most common character in the window. 

 If the operations required are within the allowed limit (<= k), continue expanding the window by moving the right pointer. Or if the operations is more than k, adjust the window by moving the left pointer forward. Repeat this process until the entire string is traversed, and return the maximum length of any valid window encountered.

**Time Complexity:** O(n): The algorithm processes each character in the string once resulting in linear time complexity.  
**Space Complexity:** O(1): The dictionary uses constant space
