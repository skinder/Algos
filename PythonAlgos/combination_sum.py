'''
Find all valid combinations of k numbers that sum up to n
Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
'''
def combinationSum3(k: int, n: int):
    res = []

    def backtrack(curr, index, total):
        if total == 0 and len(curr) == k:
            res.append(list(curr))
        elif total < 0 or len(curr) == k:
            return
        for i in range(index, 10):
            curr.append(i)
            backtrack(curr, i + 1, total - i)
            curr.remove(i)

    backtrack([], 1, n)
    return res
'''
def backtrack(candidate):
    if find_solution(candidate):
        output(candidate)
        return
    
    # iterate all possible candidates.
    for next_candidate in list_of_candidates:
        if is_valid(next_candidate):
            # try this partial candidate solution
            place(next_candidate)
            # given the candidate, explore further.
            backtrack(next_candidate)
            # backtrack
            remove(next_candidate)
'''