def champagne_tower(poured, query_row, query_glass):
    tower = [[0.0]*(i+1) for i in range(query_row+1)]
    tower[0][0] = float(poured)
    for row in range(query_row):
        for glass in range(row+1):
            excess = (tower[row][glass] - 1.0) / 2.0
            if excess > 0:
                tower[row+1][glass] += excess
                tower[row+1][glass+1] += excess
    return min(1.0, tower[query_row][query_glass])

if __name__ == "__main__":
    print(round(champagne_tower(1,1,1), 5))  # 0.00000
    print(round(champagne_tower(2,1,1), 5))  # 0.50000
