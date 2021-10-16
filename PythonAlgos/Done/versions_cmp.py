def cmp(v1,v2):
    v1_list = v1.split(".")
    v2_list = v2.split(".")
    for i in range(len(v1_list)):
        if (i > len(v2_list) - 1) or (v1_list[i] > v2_list[i]):
            return 1
        if v1_list[i] < v2_list[i]:
            return -1

    if len(v2_list) > len(v1_list):
        return -1
    else: return 0



def sort_ver(arr):
    for i in range(len(arr)):
        min = i

        for j in range(i+1, len(arr)):
            if cmp(arr[j], arr[i]) == -1:
                min = j
        arr[i], arr[min] = arr[min], arr[i]

    return arr


print sort_ver(['1.1.0.2.3','1.1.0.2.1','1.0.1','1.1.3'])