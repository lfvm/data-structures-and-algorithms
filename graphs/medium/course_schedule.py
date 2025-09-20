"""
207. Course Schedule
https://leetcode.com/problems/course-schedule/description/

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        """
            1. Build an adjacency list 
            2. Run dfs on each item of the list. If we reach to an end where a course no longer 
            has a prerequesite, that means we can finish the course. 
            3. If there is a repeated node in the path, we have a cycle, thus it can not be completed 


        """


        preRequesitesMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites: 
            preRequesitesMap[crs].append(pre)
        
        # All curses in our current dfs path 
        visited = set()

        def dfs(course):

            coursePreRequisites = preRequesitesMap[course]

            if course in visited: 
                return False 
            if len(coursePreRequisites) == 0: 
                return True 

            visited.add(course)

            for requisite in coursePreRequisites:
                # Course already exist 
                if not dfs(requisite):
                    return False 
            
            visited.remove(course)
            preRequesitesMap[course] = []
            return True
        
        for crs in range(numCourses):
            
            if not dfs(crs):
                return False
        
        return True










