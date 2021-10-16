'''
https://leetcode.com/problems/minimum-index-sum-of-two-lists/
Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.

Example 1:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".
Example 2:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["KFC", "Shogun", "Burger King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).
'''


from collections import defaultdict
class Solution(object):
    def findRestaurant(self, list1, list2):
        if not list1 or not list2:
            return []
        dict_1 = {k: v for v, k in enumerate(list1)}
        dict_2 = {k: v for v, k in enumerate(list2)}
        dict3 = defaultdict(list)
        for key in dict_1:
            if key in dict_2:
                sum_val = dict_1[key] + dict_2[key]
                dict3[sum_val].append(key)
        min_val = min(dict3.keys())
        return dict3[min_val]





a = Solution()

print a.findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"], ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"])