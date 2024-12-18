## Longest Substring Without Repeating Characters

**Problem Description:**  
Given a string `s`, find the length of the longest substring without repeating characters.

**Difficulty:** `Medium`  
**Category:** `Sliding Window`

**Example Input/Output:**  
**Input:** "abcabcbb"  
**Output:** 3  
**Explanation:**  
The longest substring without repeating characters is "abc", which has a length of 3.

---

## Solution. Sliding Window Technique

This approach uses the sliding window technique to find the length of the longest substring without repeating characters. The process involves maintaining two pointers, `left` and `right`, to define the current window, and a set to track unique characters within the window.

1. A set (char_set) is used to store unique characters within the window. Start with the `left` pointer at 0 and iterate through the string using the `right` pointer.
2. If the character at `right` is not in the set:
    - Add it to the set.
    - Calculate the window size as `right` - `left` + 1.
    - Update the max_length to store the maximum of the current and previous window sizes.
3. If the character at `right` is already in the set:
    - Shrink the window by removing characters starting from `left`.
    - Increment the `left` pointer until the duplicate character is removed from the set.
    - Repeat this process until the end of the string.

4. The final value of max_length represents the length of the longest substring without repeating characters.

Time Complexity: O(n): Each character is added to and removed from the set at most once
Space Complexity: O(min(n, m)): The set stores up to `m` unique characters or n if all characters in the string are unique.