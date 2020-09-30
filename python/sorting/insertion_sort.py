# Base case is when the list has length 0 or 1

def InsertionSort(seq):
    isort(seq, len(seq))
    return seq

def isort(seq, k):  # sort slice seq[0:k]
    if k > 1:
        isort(seq, k-1)
        insert(seq, k-1)

def insert(seq, k):  # insert seq[k] into sorted seq[0:k-1]
    pos = k
    while pos > 0 and seq[pos] < seq[pos-1]:
        (seq[pos], seq[pos-1]) = (seq[pos-1], seq[pos])
        pos -= 1

arr = [1, 4, 2, 3, 0, 5]
print(InsertionSort(arr))
