class Solution:

    def climbStairs(self, n: int) -> int:
        
        """
            We know that the number of ways to reach the top 
            is 

            The number of ways of N-1 + number of ways of N-2 
            Example: 

            To reach 3 : 

            N = 3
            We know number of ways to reach 2 are just 2 
            the number of ways to rach 1 are 1. 
            1+2 = 3 which is correct.

            IF we wanted to know for 4. The answer would be 
            3 + n ways to reach 2 which is 2. 3 + 2 = 5 
        """

        if n <= 2: 
            return n 

        first = 1
        second = 2       
        for i in range(2, n):
            res = first + second 
            first = second 
            second = res 
        return second
      
    
    #Second approach using recursion and memoization
    # def climbStairs(self, n: int) -> int:
    
    #     memo = {}

    #     def climb(n):

    #         if n <= 2: 
    #             return n
    #         elif n in memo: 
    #             return memo[n]
    #         res = climb(n-1) + climb(n-2)
    #         memo[n] = res 
    #         return res 

    #     return climb(n)
    

    
