# [Palindromic Substring](https://leetcode.com/problems/palindromic-substrings/description/)

**Problem Description:**  
Given a string s, return the number of palindromic substrings in it.

**Difficulty:** `Medium`  
**Category:** `Two Pointers`, `String`, `Dynamic Programming`

**Example Input/Output:**  
**Input:** `s = "aaa"`  
**Output:** `6`  
**Explanation:** Six palindromic substrings: "a", "a", "a", "aa", "aa", "aaa".

---

### Approach: Expanding Around the Center

This method uses the concept of expanding around the center to identify valid palindromes.

There are two types of palindromes to consider:
  1. **Odd-length palindromes** where the center is a single character.
  2. **Even-length palindromes** where the center is a pair of characters (Two adjacent characters).

Each character in the string is treated as a potential center of a palindrome. Using two pointers, we compare the characters at the left and right pointers. If the characters are equal, we increment the palindrome count and continue expanding the pointers outward by 1 until either pointer goes out of bounds. And we do this for every character in the string.

**NOTE:** The `nonlocal` keyword is used to modify a variable from an outer (but not global) scope within a nested function(expand function here). It allows the inner function to refer to and change the value of variables in the enclosing scope.