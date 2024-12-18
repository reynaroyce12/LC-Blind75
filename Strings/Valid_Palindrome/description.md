# [Valid Palindrome](https://leetcode.com/problems/Valid-Palindrome/description/)

**Problem Description:**   
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return `true` if it is a palindrome, or `false` otherwise.

**Difficulty:** `Easy`  
**Category:** `Strings`, `Two Pointers`

**Input:**  
`s = "race a car"`  
**Output:**  
`False`  
**Explanation:**  
After cleaning the string, it becomes "raceacar", which is not a palindrome.



## Solution 1. Using Reversed String

In this approach, we remove all non-alphanumeric characters from the input string and convert the string to lowercase. Then, we reverse this string and compare it with the original string with no alphanumeric characters. If they are equal, the input string is a palindrome.


1. Remove all non-alphanumeric characters and convert the string to lowercase.
2. Reverse the cleaned string using slicing (`[::-1]`).
3. Compare the original cleaned string with the reversed string:
   - If they are the same, return `True`.
   - Otherwise, return `False`.   


*Time Complexity:* O(n) Because we process each character once  
*Space Complexity:* O(n) Due to the storage required for the cleaned string and its reversed version.



## Solution 2. Using Two Pointers (Optimal Approach) 

In this approach we make use of two pointers, one which starts from the beginning of the string and increments (`left`) and the other one which starts from the end of the string and decrements (`right`). 

1. Initialize two pointers: left at the beginning of the string and right at the end.
2. While the two pointers haven't crossed:
    - Skip non-alphanumeric characters by adjusting the left and right pointers.
    - Compare the characters at the left and right pointers (ignoring case).
    - If the characters do not match, return False immediatly.
    - Otherwise, move both pointers inward.
3. If the loop completes without finding mismatched characters, return True.

*Time Complexity:* O(n) Because we traverse the string once   
*Space Complexity:* O(1) Becuase there are no additional data structures involved and we only use a fixed amount of extra space for the pointers.

