def solution(N, R, C):
    # write your code in Python 3.6
    board = [[0 for col in range(N)] for row in range(N)]
    bombs_nbr = len(R)
    for i in range(bombs_nbr):
        board[R[i]][C[i]] = 'B'

    for i in range(bombs_nbr):
        if R[i] - 1 >= 0 and board[R[i]-1][C[i]] != 'B':
            board[R[i]-1][C[i]] += 1
        if R[i] + 1 <= N-1 and board[R[i]+1][C[i]] != 'B':
            board[R[i]+1][C[i]] += 1
        if C[i] - 1 >= 0 and board[R[i]][C[i]-1] != 'B':
            board[R[i]][C[i]-1] += 1
        if C[i] + 1 <= N-1 and board[R[i]][C[i]+1] != 'B':
            board[R[i]][C[i]+1] += 1
        if R[i] - 1 >= 0 and C[i] - 1 >= 0 and board[R[i]-1][C[i]-1] != 'B':
            board[R[i]-1][C[i]-1] += 1
        if R[i] + 1 <= N-1 and C[i] + 1 <= N-1 and board[R[i]+1][C[i]+1] != 'B':
            board[R[i]+1][C[i]+1] += 1
        if R[i] - 1 >= 0 and C[i] + 1 <= N-1 and board[R[i]-1][C[i]+1] != 'B':
            board[R[i]-1][C[i]+1] += 1
        if R[i] + 1 <= N-1 and C[i] - 1 >= 0 and board[R[i]+1][C[i]-1] != 'B':
            board[R[i]+1][C[i]-1] += 1

        result_comp = [''.join([str(col) for col in row]) for row in board]


    return '\n'.join([''.join([str(col) for col in row]) for row in board])


print(solution(5,[2, 3, 2, 3, 1, 1, 3, 1], [3, 3, 1, 1, 1, 2, 2, 3]))