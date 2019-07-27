# implement count_unique_words(input_str) function -
#    returns number of unique words from the input string
# Note: For counting unique words do not ignore case


def count_unique_words(input_str):
    # code here
    unique_words = len(set(input_str.split()))
    print set(input_str.split())
    return unique_words


assert count_unique_words('') == 0
assert count_unique_words(' Hello World ') == 2
assert count_unique_words('That that is is that that is not is not is that it it is') == 5
assert count_unique_words('Can you can a     can as a canner can can a can') == 6