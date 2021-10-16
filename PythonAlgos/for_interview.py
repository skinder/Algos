import math
import random


def cmp(a, b): return (a > b) - (a < b)


"""
Loops
for x in l:  "Iterate on x for each value in list"
for i in range(0,5): "Iterate on i from value 0 to 4"
for k, v in d.items(): "Iterate on each key, value pair in dict"


Lists (Array)
l = []  "Define an empty list"
l[i]  "Return value at index i in list"
len(l) "Return length of list"
l.append(x) "Add value x to the end of list"
l.sort() "Sort values in list - in place sort, returns None"
sorted(l) "Return sorted copy of list"
x in l: "Evaluate True if x is contained in the list"


Dictionary (HashMap)
d = {}  "Define an empty Dictionary"
d[x]  "Return value for key x"
d[x] = 1 "Set value for key x to 1"
d.keys()  "Return list of keys"
d.values() "Return list of values"


Tuple
tup = ()
tup = (1,2) + tup


Other functions
reversed(n)  "reverse a list"
random.random()  "random number between 0 and 1"
random.randrange(start, stop) "Return a randomly selected element from range(start, stop)"
isinstance(x, list)     "returns True if x is instance of list"
split()    "returns a list of all the words in the string"
ceil()    "returns the smallest integer value greater than or equal to x"
"""




Solutions(follow - ups)


# implement count_unique_words(input_str) function -
#    returns number of unique words from the input string


def count_unique_words(input_str):
    if not input_str:
        return 0
    unique_words = {}
    for s in input_str.split(' '):
        if len(s.strip()) > 0:
            unique_words[s] = unique_words.get(s, 0) + 1
    return len(unique_words)


assert count_unique_words('') == 0
assert count_unique_words(' Hello World ') == 2
assert count_unique_words('That that is is that that is not is not is that it it is') == 5
assert count_unique_words('Can you can a can as a canner can can a can') == 6


# implement top_n(input_list, n) function -
#   returns top (highest) n numbers from the input list


def top_n(input_list, n):
    if not input_list or n <= 0:
        return []
    input_list.sort(reverse=True)
    return input_list[:n]


assert cmp(sorted(top_n([1, 2, 3, 5, 6, 28, 50], 5)), [3, 5, 6, 28, 50]) == 0
assert cmp(sorted(top_n([1, 2], 0)), []) == 0
assert cmp(sorted(top_n([1], 1)), [1]) == 0
assert cmp(sorted(top_n([1, 2, 3, 3], 2)), [3, 3]) == 0
assert cmp(sorted(top_n([], 50)), []) == 0
assert cmp(sorted(top_n([1, 2, 3, 5, 6, 28, 50], 8)), [1, 2, 3, 5, 6, 28, 50]) == 0


## Note: potential follow up => ask them if they know any better way to solve this?
##   hint: heap data structure is best data structure to solve such problems


# implement count_substr(input_str, sub_str) function -
#    returns the number of times the sub_str occurs in string


def count_substr(input_str, sub_str):
    if not sub_str:
        return None
    if not input_str:
        return 0
    count = 0
    slen = len(sub_str)
    for i in range(len(input_str)):
        if input_str[i:i + slen] == sub_str:
            count += 1
    return count


assert count_substr('', 'hello') == 0
assert count_substr('abcdabc', 'abc') == 2
assert count_substr('aaaaa', 'aa') == 4
assert count_substr(' hello world ', ' ') == 3


# Alternate one liner
def count_substr(input_str, sub_str):
    if len(sub_str) == 0:
        return None
    return sum([input_str[i:].startswith(sub_str) for i in range(len(input_str))])


# implement sample(input_list, n) function -
#    returns list with randomly sampled at most 'n' elements.
#    All the elements should be from the input_list and function
#    should mostly generate random values every time it is run


import random


def sample(input_list, n):
    if not input_list or n >= len(input_list):
        return input_list
    output_list = []
    random_index_list = []
    while (len(output_list) < n):
        random_index = random.randrange(0, len(input_list))
        if random_index not in random_index_list:
            output_list.append(input_list[random_index])
            random_index_list.append(random_index)
    return output_list


## you can add below function and asserts after candidate has implemented the code
def validate_sample(input_list, n):
    output_list1 = sample(input_list, n)
    if not input_list:
        return (input_list == output_list1)
    if (n > 1) and len(input_list) > n:
        output_list2 = sample(input_list, n)
        # check if both the lists are same
        if cmp(output_list1, output_list2) == 0:
            print('list1: ')
            print(output_list1)
            print('list2: ')
            print(output_list2)
            return False
    else:
        if len(output_list1) > n:
            print('list1: ')
            print(output_list1)
            return False
        for i in output_list1:
            if i not in input_list:
                print('list1: ')
                print(output_list1)
                return False
    return True


## run this multiple times to confirm if the function works fine


assert (validate_sample([1, 2, 3, 4, 5, 6, 7, 8], 4))
assert (validate_sample([-1, 1, 4, 9, 19, 234, 13, 4, 23], 3))
assert (validate_sample([15, 25, 35, 45, 55, 65, 75], 10))
assert (validate_sample([1, 1, 7, 8, 55, 2, 10], 2))


## Note: potential follow ups =>
##   is this implementation deterministic?
##   Does it handle duplicate elements?
##   Will this go into infinite loop?
##   How can you avoid it?


# implement find_pairs(input_list) function -
#    returns all possible pair of tuples from input list
#   (input can have duplicates but the output list should be unique)


def find_pairs(input_list):
    output = []
    if (len(input_list) < 2): return output
    for i in range(len(input_list)):
        alt = input_list[:]
        alt.pop(i)
        for a in alt:
            if ((input_list[i], a) not in output):
                output.append((input_list[i], a))
    return output


assert cmp(sorted(find_pairs([1, 2, 3, 4])), sorted(
    [(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])) == 0
assert cmp(sorted(find_pairs([1, 2])), sorted([(1, 2), (2, 1)])) == 0
assert cmp(find_pairs([1]), []) == 0
assert cmp(sorted(find_pairs([1, 2, 3, 1])), sorted([(1, 2), (1, 3), (1, 1), (2, 1), (2, 3), (3, 1), (3, 2)])) == 0

# with itertools - 1
import itertools


def find_pairs_i(input_list):
    if not input_list:
        return input_list
    output_list = list(itertools.permutations(input_list, 2))
    seen = set()
    unique_list = [e for e in output_list if e not in seen and not seen.add(e)]
    return unique_list


assert cmp(sorted(find_pairs_i([1, 2, 3, 4])), sorted(
    [(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])) == 0
assert cmp(sorted(find_pairs_i([1, 2])), sorted([(1, 2), (2, 1)])) == 0
assert cmp(find_pairs_i([1]), []) == 0
assert cmp(sorted(find_pairs_i([1, 2, 3, 1])), sorted([(1, 2), (1, 3), (1, 1), (2, 1), (2, 3), (3, 1), (3, 2)])) == 0

# with itertools - 2
import itertools


def find_pairs_i(input_list):
    if not input_list:
        return input_list
    output_list = []
    for pair in itertools.permutations(input_list, 2):
        if pair not in output_list:
            output_list.append(pair)
    return output_list


assert cmp(sorted(find_pairs_i([1, 2, 3, 4])), sorted(
    [(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])) == 0
assert cmp(sorted(find_pairs_i([1, 2])), sorted([(1, 2), (2, 1)])) == 0
assert cmp(find_pairs_i([1]), []) == 0
assert cmp(sorted(find_pairs_i([1, 2, 3, 1])), sorted([(1, 2), (1, 3), (1, 1), (2, 1), (2, 3), (3, 1), (3, 2)])) == 0


# implement is_numeric(string) function -
#   returns True if the string is numeric, False otherwise


def is_numeric(input_str):
    if input_str == None:
        return False
    try:
        float(input_str)
        return True
    except ValueError:
        return False


assert is_numeric('12') == True
assert is_numeric('-1') == True
assert is_numeric('+100') == True
assert is_numeric('') == False
assert is_numeric('1.2') == True
assert is_numeric('0.00023') == True
assert is_numeric('.00023') == True
assert is_numeric('3.3.3.3') == False
assert is_numeric('3. 3') == False

## Note: bonus points if they consider hexadecimals and octal numbers


For
Easy
Pasting
To
Feedback


