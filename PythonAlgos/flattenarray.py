'''
Given a nested array of values, write a function to return a flattened array containing only the integer values.
Ex.
Input: [6, 2, [1, [9, 3], [1, 2], [True], 'hello world', [None] ], 2]

Output: [6, 2, 1, 9, 3, 1, 2, 2]

'''

def flatten(arr):
    flattened = []
    for i in arr:
        if type(i) == list:
            child_flatten = flatten(i)
            for j in child_flatten:
                flattened.append(j)
        elif type(i) == int:
            flattened.append(i)

    return flattened


if __name__ == '__main__':
    test_input = [6, 2, [1, [9, 3], [1, 2], [True], 'hello world', [None]], 2]
    test_result = sorted([6, 2, 1, 9, 3, 1, 2, 2])
    result = sorted(flatten(test_input))

    print(flatten(test_input))