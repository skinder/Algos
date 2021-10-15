# N: # of strs
# M: avg len of str
def pangram(strs):
    def isPangram(string):
        alpha, count = [0 for _ in range(26)], 0
        for c in string:
            if c == ' ':
                continue
            elif alpha[ord(c) - ord('a')] == 0:
                print(c, ord(c))
                alpha[ord(c) - ord('a')] += 1
                count += 1
        return '1' if count == 26 else '0'

    res = ''
    for string in strs: # O(M*N)
        res += isPangram(string)

    return res

print(pangram(['pack my box with five dozen liquor jugs', 'this is not a pangram'])) # '10'