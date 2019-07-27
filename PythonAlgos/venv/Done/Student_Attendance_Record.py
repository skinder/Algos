'''
characters:
'A' : Absent.
'L' : Late.
'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record.

Example 1:
Input: "PPALLP"
Output: True
Example 2:
Input: "PPALLL"
Output: False
'''


class Solution(object):
    def checkRecord(self, s):
        a_cnt = 0
        for i in range(len(s)):
            if len(s) - i >= 3 and s[i:i+3] == 'LLL':
                return False
            if s[i] == 'A':
                a_cnt = a_cnt + 1
                if a_cnt > 1:
                    return False
        return True





a = Solution()

print a.checkRecord("AAAAA")
print a.checkRecord("PPALLP")
print a.checkRecord("PPALLL")
