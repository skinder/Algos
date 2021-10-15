'''
https://leetcode.com/problems/verifying-an-alien-dictionary/
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.



Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
'''

from typing import List

def isAlienSorted(words: List[str], order: str):
    order_dict = {}
    order_dict['0'] = 0
    for ind, l in enumerate(order):
        order_dict[l] = ind + 1

    for wi in range(1,len(words)):
        if len(words[wi]) > len(words[wi-1]):
            words[wi - 1] = words[wi-1].ljust(len(words[wi]),'0')
        if len(words[wi]) < len(words[wi-1]):
            words[wi] = words[wi].ljust(len(words[wi-1]),'0')
        for li in range(len(words[wi])):
            if order_dict[words[wi - 1][li]] == order_dict[words[wi][li]]:
                continue
            elif order_dict[words[wi-1][li]] < order_dict[words[wi][li]]:
                break
            elif order_dict[words[wi-1][li]] > order_dict[words[wi][li]]:
                return False
    return True

print(isAlienSorted(["app", "apple"], "worldabcefghijkmnpqstuvxyz"))
