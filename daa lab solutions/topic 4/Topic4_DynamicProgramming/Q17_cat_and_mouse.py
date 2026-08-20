from functools import lru_cache

def cat_mouse_game(graph):
    n = len(graph)
    DRAW, MOUSE_WIN, CAT_WIN = 0, 1, 2

    import sys
    sys.setrecursionlimit(10000)

    @lru_cache(maxsize=None)
    def solve(mouse, cat, turn, moves):
        if moves >= 2*n:
            return DRAW
        if mouse == 0:
            return MOUSE_WIN
        if mouse == cat:
            return CAT_WIN
        if turn == 0:  # mouse's turn
            best = CAT_WIN
            for nxt in graph[mouse]:
                res = solve(nxt, cat, 1, moves+1)
                if res == MOUSE_WIN:
                    return MOUSE_WIN
                if res == DRAW:
                    best = DRAW
            return best
        else:  # cat's turn
            best = MOUSE_WIN
            for nxt in graph[cat]:
                if nxt == 0:
                    continue
                res = solve(mouse, nxt, 0, moves+1)
                if res == CAT_WIN:
                    return CAT_WIN
                if res == DRAW:
                    best = DRAW
            return best

    return solve(1, 2, 0, 0)

if __name__ == "__main__":
    print(cat_mouse_game([[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]))  # 0
    print(cat_mouse_game([[1,3],[0],[3],[0,2]]))                       # 1
