


def print_nested_list(lst, txt):
    for i in range(len(lst)):
        if type(lst[i]) != list:
            output = txt + str(i) + " - " + str(lst[i])
            print output
        else:
            output = txt + str(i) + " - "
            print_nested_list(lst[i], output)

print_nested_list([1,2,[3,4]], "Elem: ")
