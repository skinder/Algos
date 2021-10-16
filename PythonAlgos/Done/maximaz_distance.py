'''
In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty.

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized.

Return that maximum distance to closest person.

Example 1:

Input: [1,0,0,0,1,0,1]
Output: 2
Explanation:
If Alex sits in the second open seat (seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.
Example 2:

Input: [1,0,0,0]
Output: 3
Explanation:
If Alex sits in the last seat, the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.

'''
class Solution(object):
    def maxDistToClosest(self, seats):
        first_dist = -1
        max_distance = curr_max = 0
        for i in range(len(seats)):
            if first_dist == -1 and seats[i]:
                first_dist = i
                curr_max = 0
            elif seats[i] == 1:
                max_distance = max(max_distance, (curr_max + 1))
                curr_max = 0
            else:
                curr_max += 1

        max_distance = max(max_distance // 2, curr_max, first_dist)
        return max_distance


a = Solution()

print a.maxDistToClosest([1,0,0,0,1,0,1])
print a.maxDistToClosest([0,0,0,0,1,0,0])