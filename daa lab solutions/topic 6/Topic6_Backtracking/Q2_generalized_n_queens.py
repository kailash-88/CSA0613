def solve_n_queens_general(rows, cols, obstacles=None, restricted_first_row=None):
    obstacles = obstacles or set()
    solutions = []
    used_cols = set()
    board = [-1]*rows

    def is_safe(r, c):
        if (r, c) in obstacles:
            return False
        if c in used_cols:
            return False
        for prev_r in range(r):
            prev_c = board[prev_r]
            if abs(prev_r - r) == abs(prev_c - c):
                return False
        return True

    def backtrack(r):
        if r == rows:
            solutions.append(board[:])
            return True
        col_range = range(cols)
        if r == 0 and restricted_first_row:
            col_range = [c for c in range(cols) if c not in restricted_first_row]
        for c in col_range:
            if is_safe(r, c):
                used_cols.add(c)
                board[r] = c
                if backtrack(r+1):
                    return True
                used_cols.remove(c)
                board[r] = -1
        return False

    backtrack(0)
    return solutions[0] if solutions else None

if __name__ == "__main__":
    print("8x10 board:", solve_n_queens_general(8, 10))
    print("5x5 with obstacles:", solve_n_queens_general(5, 5, obstacles={(2,2),(4,4)}))
    print("6x6 restricted first-row cols {2,4}:", solve_n_queens_general(6, 6, restricted_first_row={2,4}))
