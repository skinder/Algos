# implement sample(input_list, n) function -
#    returns list with randomly sampled at most 'n' elements.
#    All the elements should be from the input_list and function
#    should mostly generate random values every time it is run


def sample(input_list, n):
    return output_list


## validation function
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
                print ('list1: ')
                print (output_list1)
                return False
    return True


assert (validate_sample([1, 2, 3, 4, 5, 6, 7, 8], 4))
assert (validate_sample([-1, 1, 4, 9, 19, 234, 13, 4, 23], 3))
assert (validate_sample([15, 25, 35, 45, 55, 65, 75], 10))
assert (validate_sample([1, 1, 7, 8, 55, 2, 10], 2))
