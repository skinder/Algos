'''
Example 1:
Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
'''
def decodeString(s: str):
    ans = ""
    currNum = 0

    i = 0
    while i < len(s):
        c = s[i]
        if c.isdigit():
            currNum = currNum * 10 + int(c)
        elif 'a' <= c <= 'z':
            ans += c
        elif c == '[':
            count = 1
            j = i
            while count > 0:
                j += 1
                if s[j] == '[': count += 1
                if s[j] == ']': count -= 1
            temp = decodeString(s[i + 1:j])
            for _ in range(currNum): ans += temp
            currNum = 0
            i = j
        i += 1

    return ans