# Lists

# Constract list with even numbers
'''
input_list = [1, 2, 4, 6, 7, 9, 10]
output_list = []

for i in input_list:
    if i % 2 == 0:
        output_list.append(i)

print output_list

list_using_comp = [var for var in input_list if var % 2 == 0]
print list_using_comp

list_sqr = [i**2 for i in range(1,10)]

print list_sqr


input_list.append(22)
print input_list
print input_list.pop()


def revert_string(input):
    output = []
    for i in range(len(input) -1, -1, -1):
        output.append(input[i])
    return output

input_list = [1, 2, 4, 6, 7, 9, 10]
print revert_string(input_list)

'''

def return_position(line, substr):
    return line.find(substr)

def return_substring_count(line, substr):
    return line.count(substr)

def revert_string(input):
    return input[::-1]

def revert_list(input):
    output = []
    for i in range(len(input) -1, -1, -1):
        output.append(input[i])
    return output


def count_substr(input, substr):
    if not input:
        return None

    if not substr:
        return 0

    result = 0
    len_sbstr = len(substr)
    for i in range(len(input)):
        if input[i:i+len_sbstr] == substr:
            result += 1
    return result


def srt(nums2):
    print nums2.sort()

print return_position('Hello', 'lo')
print return_substring_count('AAAA', 'AA')
print revert_string('ABCD')
print revert_list(['a', 'b', 'c', 'd'])
print count_substr('AAAA', 'AA')
print srt([1,3,5,2])


a = [1,3,5,2]
print a.sort()




