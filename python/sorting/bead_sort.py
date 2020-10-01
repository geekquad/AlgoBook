"""
Bead Sort only works for sequences of Non-Negative Integers.
"""


def bead_sort(sequence: list) -> list:
    """
    >>> bead_sort([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]
    >>> bead_sort([6, 11, 12, 4, 1, 5])
    [1, 4, 5, 6, 11, 12]
    >>> bead_sort([9, 8, 7, 6, 5, 4 ,3, 2, 1])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> bead_sort([5, 0, 4, 3])
    [0, 3, 4, 5]


    """
    if any(not isinstance(x, int) or x < 0 for x in sequence):
        raise TypeError("Sequence must be list of nonnegative integers")
    for _ in range(len(sequence)):
        for i, (rod_upper, rod_lower) in enumerate(zip(sequence, sequence[1:])):
            if rod_upper > rod_lower:
                sequence[i] -= rod_upper - rod_lower
                sequence[i + 1] += rod_upper - rod_lower
    return sequence


if __name__ == "__main__":
    print(bead_sort([5, 4, 3, 2, 1]))  # OutPut => [1, 2, 3, 4, 5]
    print(bead_sort([6, 11, 12, 4, 1, 5]))  # OutPut => [1, 4, 5, 6, 11, 12]
    print(bead_sort([9, 8, 7, 6, 5, 4, 3, 2, 1])) # OutPut => [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(bead_sort([5, 0, 4, 3]))  # OutPut => [0, 3, 4, 5]
