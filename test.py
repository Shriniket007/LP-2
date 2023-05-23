def solve_N_qeen(n):
    
    def is_Safe(board, row, col):
        for i in range(row):
            if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
                return False
        return True    
    def backtrack(board, row):
        if row == n:
            return [format_solution(board)]

        solutions = []
        for col in range(n):
            if is_Safe(board, row, col):
                board[row] = col
                solutions += backtrack(board, row + 1)
        return solutions
    
    def format_solution(board):
        format_board = []
        for col in board:
            row_string = ['.']*n 
            row_string[col] = 'Q'
            format_board.append(''.join(row_string))
        return format_board
    
    return backtrack([None]*n, 0)

n = int(input("enter the size of board:"))

solutions = solve_N_qeen(n)

if solutions:
    for solution in solutions:
        for row in solution:
            print(row)
        print()

else:
    print("no sol")