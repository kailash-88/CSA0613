def solve_n_queens(n):
    solutions = []
    cols = set(); diag1 = set(); diag2 = set()
    board = [-1]*n

    def backtrack(row):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if col in cols or (row-col) in diag1 or (row+col) in diag2:
                continue
            cols.add(col); diag1.add(row-col); diag2.add(row+col)
            board[row] = col
            backtrack(row+1)
            cols.remove(col); diag1.remove(row-col); diag2.remove(row+col)

    backtrack(0)
    return solutions

def print_board(solution, n):
    for col in solution:
        row = ['.'] * n
        row[col] = 'Q'
        print(' '.join(row))
    print()

if __name__ == "__main__":
    for n in [4, 5, 8]:
        sols = solve_n_queens(n)
        print(f"N = {n}: {len(sols)} solutions found. Showing first solution:")
        print_board(sols[0], n)
