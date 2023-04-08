from collections import Counter

def smb(text, symbol):
    text_dict = Counter(text)
    return text_dict[symbol]


print(smb('ddffrrr', 'k'))