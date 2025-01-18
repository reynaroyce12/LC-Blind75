# [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/description/)

**Problem Description:**  
Given a string `s`, return the longest palindromic substring in `s`.

**Difficulty:** `Medium`  
**Category:** `String`, `Two Pointers`

**Example Input/Output:**  
**Input:** `s = "babad"`  
**Output:** `"bab"` or `"aba"`  
**Explanation:** Both "bab" and "aba" are valid answers.

---

### Approach: Expand Around Center  

This method uses the idea of expanding around the center to find the longest palindrome in the string. So each character is considered as the center of a potential palindrome and we expand towards both sides from the center till either of the pointers go out of bounds or when the characters are not equal.

We have to consider odd length palindrome as well as even length palindrome. For odd length, there will be only one center character so both `left` and `right` characters will start from the same index.

But for the even length, since there will be two center characters, the right pointer will be one next to the left pointer. `i.e if left = i then right = i + 1`

Steps:
- Iterate through each character in the string.
- For each character, treat it as the center of an odd-length palindrome (single character at the center).
- Also treat the pair of consecutive characters as the center of an even-length palindrome (two characters at the center).
- Expand outwards from these centers, checking if the substring is still a palindrome.
- Expand till either of the pointer go out of bounds or when the character at left is not equal to the character at right
- Track the longest palindrome found during the iterations.

*Time Complexity:* `O(n^2)` – We check each character and expand around it, which takes `O(n)` time, and we do this for each character (`O(n)` total).  
*Space Complexity:* `O(1)` – We only use a few extra variables to store the left and right pointers and the longest palindrome.  
