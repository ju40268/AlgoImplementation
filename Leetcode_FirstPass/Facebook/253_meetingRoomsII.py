# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        end = res = 0
        starts = sorted(i.start for i in intervals)
        ends = sorted(i.end for i in intervals)
        
        for s in range(len(intervals)):
            if starts[s] < ends[end]: 
                res += 1
            else: 
                end += 1
        return res