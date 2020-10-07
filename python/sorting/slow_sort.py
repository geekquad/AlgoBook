def SlowSort(A, i, j):
    if i >= j:
        return
    m = ((i + j) // 2)
    SlowSort(A, i, m)
    SlowSort(A, m + 1, j)
    if A[m] > A[j]:
        A[m], A[j] = A[j], A[m]
    SlowSort(A, i, j - 1)
    return A


# Example run of SlowSort
def main():
    arr = [2, 7, 9, 3, 1, 6, 5, 4, 12]
    print("Result: " + str(SlowSort(arr, 0, len(arr) - 1)))


if __name__ == "__main__":
    main()
