import heapq
from typing import List
# return the minimum number of conference rooms required
def minMeetingRooms(intervals: List[List[int]]) -> int:
    # The heap initialization
    free_rooms = []
    intervals.sort(key=lambda x: x[0])
    # Add the first meeting. We have to give a new room to the first meeting.
    heapq.heappush(free_rooms, intervals[0][1])
    # For all the remaining meeting rooms
    for i in intervals[1:]:
        # If the room due to free up the earliest is free, assign that room to this meeting.
        if free_rooms[0] <= i[0]:
            heapq.heappop(free_rooms)
        # If a new room is to be assigned, then also we add to the heap,
        # If an old room is allocated, then also we have to add to the heap with updated end time.
        heapq.heappush(free_rooms, i[1])

    return len(free_rooms)

def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort()
    result = []
    for interval in intervals:
        if result == [] or result[-1][1] < interval[0]:
            result.append(interval)
        else:
            result[-1][1] = max(result[-1][1], interval[1])
    return result

def maximumProduct(self, nums: List[int]) -> int:
    nums.sort()
    return max(nums[0]*nums[1]*nums[-1], nums[-1]*nums[-2]*nums[-3])