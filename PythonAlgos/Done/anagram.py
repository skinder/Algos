'''
def anagram(s1,s2):
    alist = list(s2)

    pos1 = 0
    stillOK = True

    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            alist[pos2] = None
        else:
            stillOK = False

        pos1 = pos1 + 1

    return stillOK

print(anagram('abcd','dcba'))

'''



# https://leetcode.com/problems/find-all-anagrams-in-a-string/
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) == len(t) and sorted(s) == sorted(t):
            return True
        else: return False

    def check_ang(self, st1, st2):
        from collections import Counter
        st1_cnt = Counter(st1)
        st2_cnt = Counter(st2)

        for i in st1_cnt:
            if st1_cnt[i] != st2_cnt[i]:
                return False
        return True

    def findAnagrams(self, s, p): #time limit exided
        result = []
        s_len = len(s)
        p_len = len(p)
        if p_len > s_len:
            return result

        for i in range(s_len):
            if len(s[i:i+p_len]) == p_len and self.check_ang(s[i:i+p_len], p):# sorted(s[i:i+p_len]) == sorted(p):
                result.append(i)

        return result


    def findAnagrams_working(self, s, p):
        from collections import defaultdict, Counter
        counter = Counter(p)
        target_num = len(counter.keys())  # number of different letters
        letter_to_num = defaultdict(int)
        cur_num = 0  # record how many different letters satisfy the condition
        l, r = 0, 0  # two pointers
        res = []
        while r < len(s):
            if s[r] not in counter:  # case 0
                l = r + 1
                letter_to_num.clear()
                cur_num = 0
                r += 1
                continue

            letter_to_num[s[r]] += 1  # add current letter by 1

            if letter_to_num[s[r]] < counter[s[r]]:  # case 1, lengthen the window
                r += 1
            elif letter_to_num[s[r]] == counter[s[r]]:  # case 2, move forward the window
                cur_num += 1
                if cur_num == target_num:
                    res.append(l)
                    letter_to_num[s[l]] -= 1
                    cur_num -= 1
                    l += 1
                r += 1

            elif letter_to_num[s[r]] > counter[s[r]]:  # case 3, shorten the window
                if letter_to_num[s[l]] == counter[s[l]]:
                    cur_num -= 1
                letter_to_num[s[l]] -= 1
                l += 1
                if letter_to_num[s[r]] == counter[s[r]]:
                    cur_num -= 1
                letter_to_num[s[r]] -= 1

        return res

a = Solution()
print (a.findAnagrams('abab', 'ab'))