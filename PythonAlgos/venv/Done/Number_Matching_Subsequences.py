'''
https://leetcode.com/problems/number-of-matching-subsequences/
Given string S and a dictionary of words words, find the number of words[i] that is a subsequence of S.

Example :
Input:
S = "abcde"
words = ["a", "bb", "acd", "ace"]
Output: 3
Explanation: There are three words in words that are a subsequence of S: "a", "acd", "ace".


I begin by creating a default dictionary of 'list' objects.
The main benefit of a default dictionary is that when you access an entry that does not yet exist, the entry
is created automatically (in this case, the value for the entry is an empty list when it is created).
I then create a 'count' variable to keep track of the number of words that are subsequences of the given string.

The first thing I do with the dictionary is populate it with all the words in the list of words.
The key for each entry is the first letter of the word. The value is the list of words that start with that letter.
Using the example in the problem, the dictionary would look like the following:

{'a': ['a', 'acd', 'ace'], 'b': ['bb']}

The next step is to iterate through each character in the given string. For each character, I access the dictionary to retrieve the list of words that start with that character. I reset the value of the entry to an empty list and then iterate through the list of words I retrieved. If the word is only a single letter, then I conclude that we have successfully found a completed subsequence and increase our 'count' by one. Otherwise, I slice off the first character and add the sliced word back to the dictionary. This time, it is added to the entry for which the key is equal to the first letter of the sliced word.

This process continues until we have iterated through all characters in the string. At the end, I return the count.
'''
from collections import defaultdict

class Solution(object):
    def numMatchingSubseq(self, S, words):
        from collections import Counter
        s_dict = Counter(S)
        output = 0
        for el in words:
            temp_s = s_dict.copy()
            temp_cnt = 0
            for i in el:
                if i in temp_s and temp_s[i] != 0:
                    temp_cnt += 1
                    temp_s[i] -= 1
                else:
                    break
            if temp_cnt == len(el):
                output += 1
        return output


    def numMatchingSubseq2(self, S, words):

        word_dict = defaultdict(list)
        count = 0

        for word in words:
            word_dict[word[0]].append(word) # {'a': ['a', 'acd', 'ace'], 'b': ['bb']}

        for char in S:
            words_expecting_char = word_dict[char]
            word_dict[char] = []
            for word in words_expecting_char:
                if len(word) == 1:
                    # Finished subsequence!
                    count += 1
                else:
                    word_dict[word[1]].append(word[1:])

        return count





a = Solution()

print a.numMatchingSubseq("abcde", ["a", "bb", "acd", "ace"])
print a.numMatchingSubseq2("abcde", ["a", "bb", "acd", "ace"])