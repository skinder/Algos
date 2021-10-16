
'''
Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.
It is guaranteed there is at least one word that isn't banned, and that the answer is unique.
Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case sensitive.  The answer is in lowercase.


Input:
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
Output: "ball"
Explanation:
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph.
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"),
and that "hit" isn't the answer even though it occurs more because it is banned.
'''

from typing import List
import re
from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> dict:
        current_max = 0
        result = ''
        words_lst = Counter(re.findall(r'\w+', paragraph.lower()))
        for i in words_lst:
            if i not in banned and words_lst[i] > current_max:
                result = i
                current_max = words_lst[i]

        return result


a = Solution()
print(a.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))