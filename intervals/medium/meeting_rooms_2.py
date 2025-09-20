"""
Meeting Rooms II
https://neetcode.io/problems/meeting-schedule-ii

Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), find the minimum number of days required to schedule all meetings without any conflicts.

Example 1:

Input: intervals = [(0,40),(5,10),(15,20)]

Output: 2
Explanation:
day1: (0,40)
day2: (5,10),(15,20)

Example 2:

Input: intervals = [(4,9)]

Output: 1
Note:

(0,8),(8,10) is not considered a conflict at 8
Constraints:

"""

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        concurrentMeetings = 0
        res = 0

        s,e = 0,0 

        while s < len(intervals):

            if start[s] < end[e]:
                concurrentMeetings += 1 
                s += 1 
            else: 
                concurrentMeetings -= 1 
                e += 1 
            
            res = max(res,concurrentMeetings )

        return res



        return res