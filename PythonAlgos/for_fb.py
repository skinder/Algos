# find the average length of word in sentence
def avg_word_len(sent):
    if len(sent.replace(" ", "")) == 0:
        return 0
    sent_list = sent.split()
    return len(sent.replace(" ", ""))/len(sent_list)

# print(avg_word_len("Hit myh nam ist Bob"))
# print(avg_word_len("   "))
# print(avg_word_len("Skinder"))

# Validate the ip address 255.0.13.22
def valid_ip(ip):
    ip_list = ip.split(".")
    if len(ip_list) != 4:
        return False
    for i in ip_list:
        if not i.isdigit() or int(i) > 255 or int(i) < 0:
            return False
    return True
'''
print(valid_ip("255.0.1"))
print(valid_ip("255.0.1.1"))
print(valid_ip("255.0.1.a"))
print(valid_ip("300.0.1.0"))
'''

# for a list array=[['D'],['A','B'],['A','C'],['C','A']] find the number of followers
def fl_nbr(fl_lst):
    res_dict = {}
    for i in fl_lst:
        if i[0] not in res_dict:
            res_dict[i[0]] = len(i) - 1
        else:
            res_dict[i[0]] += (len(i) - 1)

    for key, value in res_dict.items():
        print(f"{key}: {value}")

# fl_nbr([['D'],['A','B'],['A','C'],['C','A']])

# Mismatched sentences
from collections import Counter
def mis_sent(sent1, sent2):
    sent_1_dict = Counter(sent1.split())
    sent_2_dict = Counter(sent2.split())
    result = []
    for key, value in sent_1_dict.items():
        if key not in sent_2_dict or sent_1_dict[key] > sent_2_dict[key]:
            result.append(key)
    for key, value in sent_2_dict.items():
        if key not in sent_1_dict or sent_2_dict[key] > sent_1_dict[key]:
            result.append(key)
    return result

print(mis_sent("This is the first sentence","And this is the second sentence"))


# Best Time to Buy and Sell Stock
[7,1,5,3,6,4]
def maxProfit(prices):
    res, min_price = 0, prices[0]
    for price in prices[1:]:
        if price < min_price:
            min_price = price
        else:
            res = max(res, price - min_price)
    return res

print(maxProfit([7,1,5,3,6,4]))