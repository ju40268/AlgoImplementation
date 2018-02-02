# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        # O(nlogn), O(1)
        sorted_intervals = sorted(intervals, key=lambda x: x.start)
        for i in range(1, len(intervals)):
        	# if the prev meeting end time overlapped with latter start time, then False 
            if sorted_intervals[i - 1].end > sorted_intervals[i].start: return False
        return True