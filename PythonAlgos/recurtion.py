def generate_numbers(N, M, prefix=None):
    '''
    generate all possible combinations of M digits from numbers from range N
    '''
    if M == 0:
        print(prefix)
        return
    prefix = prefix or []
    for digit in range(N):
        prefix.append(digit)
        generate_numbers(N, M-1, prefix)
        prefix.pop()


if __name__ == '__main__':
    generate_numbers(3,2)