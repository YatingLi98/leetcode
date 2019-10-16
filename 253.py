import heapq
class Solution:
    def minMeetingRooms(self, intervals):
        if len(intervals) == 0:
            return 0
        intervals = sorted(intervals)
        rooms = []
        heapq.heappush(rooms, intervals[0][1])
        num = 1
        for interval in intervals[1:]:
            end = heapq.heappop(rooms)
            if end <= interval[0]:
                heapq.heappush(rooms, interval[1])
            else:
                num += 1
                heapq.heappush(rooms, end)
                heapq.heappush(rooms, interval[1])
        return num




s = Solution()
print(s.minMeetingRooms([[0, 30],[5, 10],[15, 20]]))

