def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False

    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, row, n):
    if row == n:
        for r in board:
            print(' '.join('Q' if x else '.' for x in r))
        print()
        return True  # You can change this to `return` if you want all solutions

    res = False
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            res = solve_n_queens(board, row + 1, n) or res
            board[row][col] = 0
    return res

n = int(input("Enter value of N for N-Queens: "))
board = [[0]*n for _ in range(n)]

if not solve_n_queens(board, 0, n):
    print("No solution exists.")

#input dalo
#kuch bhi 4 /5