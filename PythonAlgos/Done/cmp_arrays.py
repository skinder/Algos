def bnr_search(arr, x, l, r):
    if r > l:
        mid = (l + r) // 2
        if x == arr[mid]:
            return 1

        if x > arr[mid]:
            return bnr_search(arr, x, mid + 1, r)
        else:
            return bnr_search(arr, x, l, mid - 1)
    else:
        return -1




def intersection(arr1, arr2, ln1, ln2):
    fin_arr = []
    if ln1 >= ln2:
        for i in range(ln1):
            if bnr_search(arr2,arr1[i],0,ln2) == 1:
                fin_arr.append(arr1[i])
    else:
        for i in range(ln2):
            if bnr_search(arr1,arr2[i],0,ln1) == 1:
                fin_arr.append(arr2[i])

    return fin_arr


a1 = [1,2,3,4,4]
a2 = [3,4,5,6,7,8]
len_a1 = len(a1)
len_a2 = len(a2)

print intersection(a1, a2, len_a1, len_a2)

#print bnr_search(a2,6,0,len_a2-1)

set1 = set(a1)
set2 = set(a2)

for i in set1 & set2:
    print i


