'''
https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
In a list of songs, the i-th song has a duration of time[i] seconds.

Return the number of pairs of songs for which their total duration in seconds is divisible by 60.  Formally, we want the number of indices i < j with (time[i] + time[j]) % 60 == 0.



Example 1:

Input: [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60
Example 2:

Input: [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.

'''

from collections import defaultdict


class Solution(object):
    def numPairsDivisibleBy60(self, time):

        d = defaultdict(int)

        for i in time: d[i % 60] += 1

        cnt = 0

        for k, v in d.items():

            if k == 0 or k == 30:
                cnt += v * (v - 1) // 2
            elif (60 - k) in d and (60 - k) > k:
                cnt += v * d[(60 - k)]

        return cnt


a = Solution()

print a.numPairsDivisibleBy60([30,20,150,100,40])