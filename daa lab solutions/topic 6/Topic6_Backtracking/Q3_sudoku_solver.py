def solve_sudoku(board):
    def is_valid(r, c, val):
        for i in range(9):
            if board[r][i] == val or board[i][c] == val:
                return False
        br, bc = 3*(r//3), 3*(c//3)
        for i in range(br, br+3):
            for j in range(bc, bc+3):
                if board[i][j] == val:
                    return False
        return True

    def backtrack():
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    for val in '123456789':
                        if is_valid(r, c, val):
                            board[r][c] = val
                            if backtrack():
                                return True
                            board[r][c] = '.'
                    return False
        return True

    backtrack()
    return board

if __name__ == "__main__":
    board = [
        list("53..7...."), list("6..195..."), list(".98....6."),
        list("8...6...3"), list("4..8.3..1"), list("7...2...6"),
        list(".6....28."), list("...419..5"), list("....8..79"),
    ]
    solved = solve_sudoku(board)
    for row in solved:
        print(''.join(row))
