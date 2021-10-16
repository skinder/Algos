from collections import Counter

def groupMovies(movies):
    # Write your code here
    movies_dict = Counter(movies)
    # create a hash map, key = product, value = count
    '''
        for prod in transactions:
        if prod not in count:
            count[prod] = 0
        count[prod] += 1
    '''
    # perform a 2 way sort, descending by count, increasing by product name
    ans = sorted(movies_dict.items(), key=lambda x: (-x[1], x[0]))
    ans = [str(i) + " " + str(j) for i, j in ans]
    return ans


print(groupMovies(["Luca", "Luca", "Loki", "Mandalorian", "Mandalorian"]))