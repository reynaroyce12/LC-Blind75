## Valid Parentheses

**Problem Description**  
Given a string `s` containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.  
An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

**Difficulty:** `Easy`
**Category:** `Stack`

**Example Input/Output:**  
**Input:** "()[]{}"  
**Output:** true  
**Explanation:**  
The parentheses are correctly matched and closed in the right order.

---

## Solution. Using a Stack

**Explanation:**  
We can make use of a stack to keep track of opening brackets. First we traverse through the string characters and when we encounter a opening bracket, we push it to the stack. Then when we encounter a closing bracket, we check if the top of the stack matches the corresponding opening bracket. This is done with the help of a dictionary which stores every valid pair. If it does, we pop the stack; otherwise, we return false. At the end, if the stack is empty, the string is valid.

*Steps:*
1. Iterate through each character in the string.
2. Push every opening bracket ('(', '{', '[') onto the stack.
3. For every closing bracket (')', '}', ']'), check if the stack is empty. If it is, return false. Otherwise, pop the stack and check if it matches the corresponding opening bracket.
4. After processing all characters, if the stack is empty, the string is valid; otherwise, it's invalid.

*Time Complexity:* \(O(n)\): We traverse through the string once, where \(n\) is the length of the string.  
*Space Complexity:* \(O(n)\): In the worst case, the stack can hold all opening brackets, so the space complexity is proportional to the length of the string.
