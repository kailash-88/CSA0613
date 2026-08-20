import bisect

def job_scheduling(startTime, endTime, profit):
    jobs = sorted(zip(endTime, startTime, profit))
    ends = [j[0] for j in jobs]
    n = len(jobs)
    dp = [0]*(n+1)
    for i in range(1, n+1):
        end, start, p = jobs[i-1]
        idx = bisect.bisect_right(ends, start, 0, i-1)
        dp[i] = max(dp[i-1], dp[idx] + p)
    return dp[n]

if __name__ == "__main__":
    print(job_scheduling([1,2,3,3], [3,4,5,6], [50,10,40,70]))          # 120
    print(job_scheduling([1,2,3,4,6], [3,5,10,6,9], [20,20,100,70,60])) # 150
