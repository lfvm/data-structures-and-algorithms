"""
746. Min Cost Climbing Stairs
https://leetcode.com/problems/min-cost-climbing-stairs/description/

You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

 

Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
Example 2:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.

"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        #Since the cost[-1] still needs to be counted before reaching the top 
        cost.append(0)

        """
            This is a top down dp approach. 
            On each step we can ask the question what is the min cost to reach top ? 

            that will be 
            dp[i] = dp[i] + min(dp[i+1], min(dp[i+2]))

            two decisions since we can take 1 or two steps. 

            In the end the answer will be the min of the first to elements in the array
        """

        for i in range(len(cost)-3, -1,-1):
            cost[i] = cost[i] + min(cost[i+1] , cost[i+2])
        return min(cost[i], cost[i+1])