# [Merge Sorted Linked List](https://leetcode.com/problems/merge-two-sorted-lists/description/)

**Problem Description:**  
Given the heads of two sorted linked lists `list1` and `list2`, merge the two lists into one sorted linked list. The merged list should be made by splicing together the nodes of the first two lists.

Difficulty: `Easy`  
Category: `Linked List`

**Example Input/Output:**  
**Input:**  
`list1 = [1, 2, 4]`  
`list2 = [1, 3, 4]`  
**Output:**  
`[1, 1, 2, 3, 4, 4]`  
**Explanation:**  
The merged list is formed by combining the elements of the two lists in sorted order.

## Solution. Iterative Approach

In this approach, we traverse through both linked lists, comparing the values of the current nodes in each list. To build the merged list, we use a dummy node that acts as a placeholder, allowing us to easily append nodes without needing special handling for the head. At each step, we compare the values from both lists and add the smaller value to the dummy node's next pointer. We then move the corresponding pointer of the list from which the value was taken. This process continues until both lists have been fully traversed.

Once one of the lists is emptied, any remaining nodes from the other list, which are already sorted, are appended directly to the dummy node. Finally, we return the merged list starting from the node after the dummy node, which starts from `dummy_node.next` as the dummy itself is just a placeholder.


1. Initialize a dummy node.
2. Compare the current nodes of `list1` and `list2`:
   - If the value of `list1` is smaller, append it to the result list (dummy) and move the pointer in `list1`.
   - If the value of `list2` is smaller, append it to the result list and move the pointer in `list2`.
3. Once one of the lists is fully traversed, append the remaining elements from the other list to the result list.
4. At last, Return `dummy_node.next`

*Time Complexity:* O(n)  
*Space Complexity:* O(1) (excluding the result list)
