'''
https://leetcode.com/problems/meeting-rooms-ii/
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1
'''
import heapq
from typing import List
def minMeetingRooms(intervals: List[List[int]]) -> int:
    # If there is no meeting to schedule then no room needs to be allocated.
    if not intervals:
        return 0

    # The heap initialization
    free_rooms = []

    # Sort the meetings in increasing order of their start time.
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

    # The size of the heap tells us the minimum rooms required for all the meetings.
    return len(free_rooms)

'''
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.
'''
def get_rooms_sort(intervals):
    rooms_nbr = []
    intervals.sort(key=lambda x: x[0])
    rooms_nbr.append(intervals[0][1])
    for i in intervals[1:]:
        if rooms_nbr[-1] <= i[0]:
            rooms_nbr.pop()
        rooms_nbr.append(i[1])
        rooms_nbr.sort(reverse=True)
    return len(rooms_nbr)


def canAttendMeetings(intervals: List[List[int]]) -> bool:
    '''
    Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.
    Input: intervals = [[0,30],[5,10],[15,20]]
    Output: false
    :param self:
    :param intervals:
    :return:
    '''
    if len(intervals) ==1:
        return True

    intervals.sort(key=lambda x: x[0])
    print(intervals)

    for i in range(1,len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return False

    return True



# print(canAttendMeetings([[7,10],[2,4]]))
#print(minMeetingRooms([[0,30],[5,10],[15,20]]))

print(get_rooms_sort([[0,30],[5,10],[15,20],[1,4],[2,5]]))