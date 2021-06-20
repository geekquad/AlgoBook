# class Job to store an identifier, a deadline, and the profit associated with it
class Job:
    def __init__(self, task_id, deadline, profit):
        self.task_id = task_id
        self.deadline = deadline
        self.profit = profit

def sequence_jobs(jobs, T):
    # max profit that's earned
    profit = 0

    # store used and unused slot info
    slot = [-1] * T

    # arrange jobs in decreasing order of profit
    jobs.sort(key=lambda x: x.profit, reverse=True)

    for job in jobs:
        # search for next free slot and map task to that
        for j in reversed(range(job.deadline)):
            if j < T and slot[j] == -1:
                slot[j] = job.task_id
                profit += job.profit
                break

    # print the job sequence and profit
    print("The jobs selected (in order of execution): ", list(filter(lambda a: a != -1, slot)))
    print("The total profit earned : ", profit)


# sample input
# if __name__ == '__main__':
#
#     jobs = [
#         Job(1, 3, 15), Job(2, 2, 1),
#         Job(3, 1, 20), Job(4, 5, 10),
#         Job(5, 8, 25), Job(6, 2, 20),
#         Job(7, 5, 5), Job(8, 15, 1),
#         Job(9, 9, 12), Job(10, 1, 5)
#     ]
#
#     T = 15
#
#     sequence_jobs(jobs, T)