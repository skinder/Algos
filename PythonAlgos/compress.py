'''
compress AAB -> 2A1B
'AAAAABBBCC' 5A3B1C
'ABBC' -> 1A2B1C
'''

def compress(input):
    output_list = []
    counter = 1
    input_len = len(input)
    i = 1
    while i < input_len:
        if input[i] == input[i-1]:
            counter += 1
            i += 1
        else:
            output_list.append(str(counter) + input[i-1])
            counter = 1
            i += 1
    output_list.append(str(counter) + input[i - 1])
    return ''.join(output_list)


print(compress('AAAAABBBCC'))