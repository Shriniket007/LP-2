def solve_nqueens(n):
    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
                return False
        return True

    def backtrack(board, row):
        if row == n:
            return [format_solution(board)]

        solutions = []
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                solutions += backtrack(board, row + 1)
        return solutions

    def format_solution(board):
        formatted_board = []
        for col in board:
            row_string = ['.'] * n
            row_string[col] = 'Q'
            formatted_board.append(''.join(row_string))
        return formatted_board

    return backtrack([None] * n, 0)


# Get user input for board size
n = int(input("Enter the board size: "))

solutions = solve_nqueens(n)

if solutions:
    for solution in solutions:
        for row in solution:
            print(row)
        print()
else:
    print("No solution found.")


# The first function that is executed in the program is the solve_nqueens function. This function is called with the provided board size (n) as an argument.

# Inside the solve_nqueens function, the backtrack function is called with an initial empty board and the starting row index of 0. The backtrack function is responsible for finding all possible solutions to the N-Queens problem using backtracking.

# Within the backtrack function, the base case is checked: if the current row is equal to n, it means that all queens have been successfully placed on the board. In this case, the format_solution function is called to convert the board into a formatted solution representation, and the solution is added to the list of solutions.

# If the base case is not met, the function proceeds to iterate through each column of the current row. For each column, it checks if it is safe to place a queen at that position using the is_safe function. If it is safe, the queen is placed at that position on the board, and the backtrack function is called recursively with the next row.

# The recursion continues until all rows have been processed and all possible queen placements have been explored. The function collects all the solutions found during the recursive process and returns the final list of solutions.

# Finally, in the main part of the code, the solve_nqueens function is called, and the returned solutions are stored in the solutions variable. If solutions are found, they are printed out by iterating through each solution and printing each row of the formatted board representation. If no solution is found, it prints "No solution found."
