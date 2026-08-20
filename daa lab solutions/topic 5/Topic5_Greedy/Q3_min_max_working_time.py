def min_max_working_time(jobs, k):
    def can_assign(max_time):
        workers = [0]*k
        def backtrack(i):
            if i == len(jobs):
                return True
            for w in range(k):
                if workers[w] + jobs[i] <= max_time:
                    workers[w] += jobs[i]
                    if backtrack(i+1):
                        return True
                    workers[w] -= jobs[i]
                if workers[w] == 0:
                    break
            return False
        return backtrack(0)

    jobs.sort(reverse=True)
    lo, hi = max(jobs), sum(jobs)
    while lo < hi:
        mid = (lo + hi) // 2
        if can_assign(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo

if __name__ == "__main__":
    print(min_max_working_time([3,2,3], 3))       # 3
    print(min_max_working_time([1,2,4,7,8], 2))   # 11
