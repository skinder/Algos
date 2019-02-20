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
           if ((input_list[i],a) not in output):
               output.append((input_list[i],a))
   return output


if __name__ == '__main__':
    print find_pairs([1, 2, 3, 4])
    assert cmp(sorted(find_pairs([1, 2, 3, 4])), sorted(
        [(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])) == 0
