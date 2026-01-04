"""
https://leetcode.com/problems/arranging-coins/

Description
You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

Return the number of complete rows of the staircase you will build.

Example 1:

#
# #
#

Input: n = 4

Output: 2
Example 2:

#
# #
# # #
# # #

Input: n = 9

Output: 3

"""



class Solution:

    #Binary search 
    def arrangeCoins(self, n: int) -> int:
        # We could potentially have n incomplete rows, thats why we can use it as upper bound
        # We will always have at least one row
        l,r = 1, n 
        res = 0 

        # Using gauss formula, we know how many coins we would need to have to fill row at level n
        # For example at row 3 we would need 6 coins to fill everything up. 
        # if we sum 1 + 2 + 3 we get 6. To do the sum in O(1) instead of iterative O(n) we can use gauss
        # where totalCoinsNeeded = (n/2) * (n+1).
        # Using this logic we can do a binary search until we find the first row which can be filled 
        # with the given N coins 

        while l <= r: 

            mid = (r+l) // 2
            totalCoinsNeeded = (mid/2) * (mid+1)

            if totalCoinsNeeded > n: 
                r = mid - 1
            else: 
                res = max(res,mid)
                l = mid  + 1 

        return res


    # Naive O(n)
    # def arrangeCoins(self, n: int) -> int:

    #     remaining = n
    #     rows = 0  

    #     for i in range(1,n +1):
    
    #         remaining -= i
    #         if remaining >= 0: 
    #             rows += 1  
    #         else: 
    #             break 



        
    #     return rows 





        