def job_scheduling(jobs, n):
    # Sort jobs by profit (Greedy step)
    jobs.sort(key=lambda x: x[2], reverse=True)

    result = [False] * n
    job_order = [''] * n
    total_profit = 0

    for job in jobs:
        for j in range(min(n, job[1]) - 1, -1, -1):
            if not result[j]:
                result[j] = True
                job_order[j] = job[0]
                total_profit += job[2]
                break

    print("Job order:", ' -> '.join([j for j in job_order if j]))
    print("Total profit:", total_profit)

n = int(input("Enter number of jobs: "))
jobs = []

for i in range(n):
    job_id = input(f"Job {i+1} ID: ")
    deadline = int(input("Deadline: "))
    profit = int(input("Profit: "))
    jobs.append((job_id, deadline, profit))

job_scheduling(jobs, n)

#input dalo ye
# Enter number of jobs: 4
# Job 1 ID: A
# Deadline: 2
# Profit: 100
# Job 2 ID: B
# Deadline: 1
# Profit: 19
# Job 3 ID: C
# Deadline: 2
# Profit: 27
# Job 4 ID: D
# Deadline: 1
# Profit: 25
