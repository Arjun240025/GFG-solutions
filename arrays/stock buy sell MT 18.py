# Stock Buy and Sell – Multiple Transaction Allowed
# Solved
# Difficulty: MediumAccuracy: 13.43%Submissions: 210K+Points: 4
# Given an integer array prices[], where prices[i] is the price of a given stock on the ith day. Each day you may decide to either buy or sell the stock at price[i], you can even buy and sell the stock on the same day, return the maximum profit that you can get.

# Note: A stock can only be sold if it has been bought previously and multiple stocks cannot be held on any given day.

# Examples:

# Input: prices[] = [100, 180, 260, 310, 40, 535, 695]
# Output: 865
# Explanation: Buy the stock on day 0 and sell it on day 3 => 310 – 100 = 210. Buy the stock on day 4 and sell it on day 6 => 695 – 40 = 655. Maximum Profit = 210 + 655 = 865.

class Solution:
    def maximumProfit(self, prices):
        profit = 0  # Stores the total profit

        # Check each day's price with the previous day's price
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]  # Add the profit

        return profit  # Return the total profit