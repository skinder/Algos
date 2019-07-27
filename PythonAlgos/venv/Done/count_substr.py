# implement count_substr(input_str, sub_str) function -
#    returns the number of times the sub_str occurs in string


def count_substr(input_str, sub_str):
    if not input_str:
        return None
    if not sub_str:
        return 0
    count_sub_str = 0
    sub_len = len(sub_str)
    for i in range(len(input_str)):
        if input_str[i:i + sub_len] == sub_str:
            count_sub_str += 1
    print count_sub_str
    return count_sub_str



assert count_substr('', 'hello') == None
assert count_substr('abcdabc', 'abc') == 2
assert count_substr('aaaa', 'aa') == 3
assert count_substr(' hello world ', ' ') == 3
assert count_substr(' hello world ', '') == 0
