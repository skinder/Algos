# implement top_n(input_list, n) function -
#   returns top (largest) n numbers from the input list


def top_n(input_list, n):
    if n == 0:
        return []
    input_list.sort()
    output_list = input_list[-n:]
    print output_list
    return output_list


assert cmp(sorted(top_n([1, 2, 3, 5, 6, 28, 50], 5)), [3, 5, 6, 28, 50]) == 0
assert cmp(sorted(top_n([1, 2], 0)), []) == 0
assert cmp(sorted(top_n([1], 1)), [1]) == 0
assert cmp(sorted(top_n([1, 2, 3, 3], 2)), [3, 3]) == 0
assert cmp(sorted(top_n([], 50)), []) == 0
assert cmp(sorted(top_n([1, 2, 3, 5, 6, 28, 50], 8)), [1, 2, 3, 5, 6, 28, 50]) == 0