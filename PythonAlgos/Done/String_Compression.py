'''
Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place, return the new length of the array.


Follow up:
Could you solve it using only O(1) extra space?


Example 1:

Input:
["a","a","b","b","c","c","c"]

Output:
Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

Explanation:
"aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".


Example 2:

Input:
["a"]

Output:
Return 1, and the first 1 characters of the input array should be: ["a"]

Explanation:
Nothing is replaced.


Example 3:

Input:
["a","b","b","b","b","b","b","b","b","b","b","b","b"]

Output:
Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].

Explanation:
Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
Notice each digit has it's own entry in the array.

'''


class Solution(object):
    def compress(self, chars):
        chars.append(" ")
        ln = len(chars)
        char = ''
        curr = 1
        if ln == 1:
            return 1

        for i in range(1, ln):
            if chars[i - 1] == chars[i]:
                curr += 1
                char = chars[i]
            else:
                if curr == 1:
                    chars.append(chars[i-1])
                    curr = 1
                    char = ''
                else:
                    chars.append(char)
                    for nbr in str(curr):
                        chars.append(nbr)
                    curr = 1
                    char = ''
        del chars[:ln]

        return len(chars)


a = Solution()

print a.compress(["a","a","b","b","c","c","c"])
print a.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"])
print a.compress(["a"])

