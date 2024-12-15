# [Valid Anagram](https://leetcode.com/problems/valid-anagram/description/)

**Problem Description:**   
Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise. 

An anagram is a word or phrase formed by rearranging the letters of another, typically using all the original letters exactly once.

**Difficulty:** `Easy`  
**Category:** `String`


**Example Input/Output:**  
**Input:** s = "listen", t = "silent"  
**Output:** true  
**Explanation:** "silent" can be formed by rearranging the letters of "listen".

**Input:** s = "rat", t = "car"  
**Output:** false  
**Explanation:** "car" cannot be formed by rearranging the letters of "rat".

NOTE: **Both of these solution offer the same time and space complexity. Another approach is to sort both the strings and compare them. Since sorting anagram strings produce the same result, we can check for equality. But this approach takes a time complexity of **O(n log n)** and space complexity of O(n) hence not an optimal solution.**

## Solution 1. Using Dictionary

In this method, we manually compute the frequency of characters in both strings and compare the resulting dictionaries.  

1. First, we check if the lengths of `s` and `t` are equal. If not, return `false` immediately.  
2. We create two dictionaries, `s_frequency` and `t_frequency`, to count the occurrences of each character in `s` and `t`.  
3. Then using the get method, we check if the character is already in the dictionary. If its present, it returns the associated count and if not, it returns a default value of 0. This ensures that when the character is encountered for the first time, its count starts at 0. Then, 1 is added to this value, and the updated count is assigned back to the dictionary for the character. 
3. After populating both dictionaries, we check if they are equal. If they are, `t` is an anagram of `s`.

*Time Complexity:* O(n), where `n` is the length of `s` or `t`. Each string is traversed once to calculate character frequencies.    
*Space Complexity:* O(1), assuming the character set is fixed

## Solution 2. Using Counter from Collections

In this approach, we use the `Counter` class from the `collections` built-in python module.

1. We create `Counter` objects for both `s` and `t`.  
2. We then directly compare the two `Counter` objects. If they are equal, `t` is an anagram of `s`.



*Time Complexity:* O(n), where `n` is the length of `s` or `t`. The `Counter` function internally traverses the strings to calculate frequencies.  
*Space Complexity:* O(1)