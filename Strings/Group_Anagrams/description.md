# [Group Anagrams](https://leetcode.com/problems/group-anagrams/description/)

**Problem Description:**  
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

**Difficulty:** `Medium`  
**Category:** `String`, `Hash Table`, `Sorting`

**Example Input/Output:**  
**Input:** `strs = ["eat", "tea", "tan", "ate", "nat", "bat"]`  
**Output:** `[["eat","tea","ate"],["tan","nat"],["bat"]]`  
**Explanation:**  
- The first group contains the words "eat", "tea", and "ate" which are anagrams.
- The second group contains the words "tan" and "nat" which are anagrams.
- The third group contains the word "bat" which has no anagram in the list.


`TO NOTE:` Anagrams have same character frequency


---

### Solution 1: Using Sorting  

This method uses sorting to group anagrams.
- For each word in the array, use the Counter method to calculate the frequency of each character.
- Convert the Counter object to a tuple of its items (character-frequency pairs), as tuples are hashable and can be used as dictionary keys.
- Check if this frequency tuple is already in the dictionary:
    - If it exists, append the word to the list of anagrams associated with that frequency tuple.
    - If it doesn't exist, create a new key in the dictionary and add the word as the first element in the list.
- Finally, return the values of the dictionary, which will be the grouped anagrams.

*Time Complexity:* `O(nk log k)` – Sorting each word takes `O(k log k)` time, where `n` is the number of words, and `k` is the maximum length of a word.  
*Space Complexity:* `O(nk)` – Storing up to `n` words with each word having a length of `k` in the result.

---

### Solution 2: Using Character Frequency Count  

This approach uses a fixed-size array to count character frequencies and group anagrams:  
- For each word, we create a fixed-size frequency array of 26 elements (one for each letter of the alphabet).
- For each character in the word, we increment the corresponding index in the frequency array (based on the letter's position in the alphabet).
- We then use this frequency array as a key in a dictionary to group words that have identical character counts.
- Since anagrams have identical character frequencies, words with the same frequency array will be grouped together under the same key.

*Time Complexity:* `O(nk)` – Each word is processed in linear time with respect to its length `k`, and there are `n` words.  
*Space Complexity:* `O(nk)` – Storing up to `n` words, each of length `k`, and using the frequency array as keys.
