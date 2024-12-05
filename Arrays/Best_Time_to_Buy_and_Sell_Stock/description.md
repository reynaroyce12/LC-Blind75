## Best Time to Buy and Sell Stock

**Problem Description:**  
You are given an array `prices` where `prices[i]` is the price of a given stock on the `ith day`.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



**Difficulty:** `Easy`

**Example Input/Output:**  
**Input:** [2, 4, 1]  
**Output:** 2  
**Explanation:**  
Buy on day 0 (price = 2) and sell on day 1 (price = 4), profit = 4 - 2 = 2.  
No other transactions can achieve a higher profit.


## Solution: Iterative Approach with Min Tracking

This approach involves iterating through the `prices` array and maintaining two key variables:  
1. `min_price` - Tracks the lowest price encountered so far.  
2. `max_profit` - Tracks the maximum profit that can be achieved by selling after buying at `min_price`.

For each price in the array:  
- Update `min_price` if the current price is lower.  
- Calculate the potential profit as `current_price - min_price`.  
- Update `max_profit` if the potential profit is greater than the current `max_profit`.

This ensures that we calculate the best possible profit in a single pass through the array.

*Time Complexity:* \(O(n)\): We iterate through the `prices` array once.  
*Space Complexity:* \(O(1)\): Only constant extra space is used for the variables `min_price` and `max_profit`.
