a = {'A':[], 'B':0, 'C':''}
lst = ['o','b']

for i in lst:
    a['A'].append(i)
    a['B'] += 1
    a['C'] += i
print(a)
