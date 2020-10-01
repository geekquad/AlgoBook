"""
This is a type of divide and conquer algorithm which divides the search space into
3 parts and finds the target value based on the property of the array or list.

Time Complexity  : O(log3 N)

Example :
10,20,30,50
30
Iterative search: 30 found at positions: 2
Recursive search: 30 found at positions: 2
"""
import sys

# This is the precision for this function which can be altered.
# It is recommended for users to keep this number greater than or equal to 10.
precision = 10


# This is the linear search that will occur after the search space has become smaller.
def linear_search(left, right, A, target):
    for i in range(left, right + 1):
        if A[i] == target:
            return i


# Iterative Ternary Search Algorithm

def iterative_ternary_search(A, target):
    left = 0
    right = len(A) - 1
    while True:
        if left < right:

            if right - left < precision:
                return linear_search(left, right, A, target)

            oneThird = (left + right) / 3 + 1
            twoThird = 2 * (left + right) / 3 + 1

            if A[oneThird] == target:
                return oneThird
            elif A[twoThird] == target:
                return twoThird

            elif target < A[oneThird]:
                right = oneThird - 1
            elif A[twoThird] < target:
                left = twoThird + 1

            else:
                left = oneThird + 1
                right = twoThird - 1
        else:
            return None


# Recursive Ternary Search Algorithm

def recursive_ternary_search(left, right, A, target):
    if left < right:

        if right - left < precision:
            return linear_search(left, right, A, target)

        oneThird = (left + right) / 3 + 1
        twoThird = 2 * (left + right) / 3 + 1

        if A[oneThird] == target:
            return oneThird
        elif A[twoThird] == target:
            return twoThird

        elif target < A[oneThird]:
            return recursive_ternary_search(left, oneThird - 1, A, target)
        elif A[twoThird] < target:
            return recursive_ternary_search(twoThird + 1, right, A, target)

        else:
            return recursive_ternary_search(oneThird + 1, twoThird - 1, A, target)
    else:
        return None


# Check if the array is sorted

def __assert_sorted(collection):
    if collection != sorted(collection):
        raise ValueError("Collection must be sorted")
    return True


if __name__ == "__main__":
    user_input = input(
        "Enter numbers in sorted way, separated by coma:\n").strip()
    collection = [int(item) for item in user_input.split(",")]

    try:
        __assert_sorted(collection)
    except ValueError:
        sys.exit("Sequence must be sorted to apply the ternary search")

    target_input = input("Enter a single number to be found in the list:\n")
    target = int(target_input)
    result1 = iterative_ternary_search(collection, target)
    result2 = recursive_ternary_search(
        0, len(collection) - 1, collection, target)

    if result2 is not None:
        print(f"Iterative search: {target} found at positions: {result1}")
        print(f"Recursive search: {target} found at positions: {result2}")
    else:
        print("Not found")
