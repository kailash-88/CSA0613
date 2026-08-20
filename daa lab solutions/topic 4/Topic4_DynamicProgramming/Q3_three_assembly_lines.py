# Minimize total production time across 3 lines with station-to-station
# transfer costs and sequential dependencies between stations 0->1->2.
def three_line_min_time(station_times, transfer_times):
    lines = len(station_times)
    stations = len(station_times[0])
    dp = [[0]*lines for _ in range(stations)]
    for line in range(lines):
        dp[0][line] = station_times[line][0]
    for s in range(1, stations):
        for line in range(lines):
            best = dp[s-1][line]
            for other in range(lines):
                if other != line:
                    best = min(best, dp[s-1][other] + transfer_times[other][line])
            dp[s][line] = best + station_times[line][s]
    return min(dp[stations-1])

if __name__ == "__main__":
    station_times = [[5,9,3], [6,8,4], [7,6,5]]
    transfer_times = [[0,2,3], [2,0,4], [3,4,0]]
    print("Minimum total production time:", three_line_min_time(station_times, transfer_times))
