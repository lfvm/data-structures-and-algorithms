"""
Meeting Rooms
https://neetcode.io/problems/meeting-schedule

Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), determine if a person could add all meetings to their schedule without any conflicts.

Explanation:

(0,30) and (5,10) will conflict
(0,30) and (15,20) will conflict
Example 2:

Input: intervals = [(5,8),(9,15)]

Output: true
Note:

(0,8),(8,10) is not considered a conflict at 8

"""


"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        if len(intervals) < 1:
            return True

        intervals.sort(key=lambda x: x.start)   

        # A meeting must start equal or after the previous one 

        for i in range(1, len(intervals)):

            curr = intervals[i]
            prev = intervals[i-1]

            if curr.start < prev.end:
                return False
        return True
