import collections as col
from operator import itemgetter


n = int(input("Enter the number of jobs : "))

print("Enter the details of each job : ")

Job = col.namedtuple('Job' , ['id' , 'deadline' , 'profit'])
jobSequence = []

for i in range(n):
    iD , deadline , profit = input().split(" ")
    deadline = int(deadline)
    profit = int(profit)
    job = Job(iD , deadline , profit)
    jobSequence.append(job)

jobSequence = sorted(jobSequence, key=itemgetter(Job._fields.index('profit')) , reverse = True)

maxDeadline = 0

for i in range(n):
    if jobSequence[i].deadline > maxDeadline:
        maxDeadline = jobSequence[i].deadline


availableDeadline = [1 for i in range(maxDeadline)]

totalProfit = 0
sequenceId = []

for i in range(n):

    deadlineLimit = jobSequence[i].deadline 
    
    # For each job , find the highest deadline to which it can be assigned
    for j in range(deadlineLimit):
        if availableDeadline[deadlineLimit - 1 - j] == 1:
            availableDeadline[deadlineLimit - 1 - j] = 0
            totalProfit += jobSequence[i].profit
            sequenceId.append(jobSequence[i].id)
            break



print("The total profit is : " , totalProfit)
print("The sequence of the jobs : " , *sequenceId)


