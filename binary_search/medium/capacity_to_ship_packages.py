class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        """
            Binary search problem, we now that at least we are going to need 
            max(weights) weight to be able to move all of the ships within the given days. 

            Similarly we now that the maximum value we would ever need in the worst case 
            would be to use the sum of al weights. 

            Given this constraints: min weight possible: max(weights), maximum w possible: sum(weights)

            We could perform a binary search to compute the result  

        """

        l, r = max(weights), sum(weights)
        res = r

        # Given a capacity we need to know if we can ship everything 
        # On less or equal days needed to move everything 
        def canShip(capacity):

            ships,currCap  = 1,0 
            for w in weights: 
                if currCap +  w > capacity:
                    currCap = 0
                    ships += 1
                currCap += w 

            return ships <= days 



        while l <= r: 

            capacity = (l + r) // 2 

            if canShip(capacity):
                res = min(res,capacity)
                r = capacity - 1 
            else: 
                l = capacity + 1 


        return res