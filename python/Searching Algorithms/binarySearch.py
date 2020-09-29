# Recursive Algortihm

def binarySearchRecur(arr, low, high, x):

    # Check base case
    if high >= low:

        mid = (high + low) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binarySearchRecur(arr, low, mid - 1, x)

        # Else the element can only be present in right subarray
        else:
            return binarySearchRecur(arr, mid + 1, high, x)

    else:
        # Element is not present in the array
        return -1


# Test array
arr = [20, 3, 4, 10, 40]
x = 4  # Output => 2

# Function call
result = binarySearchRecur(arr, 0, len(arr)-1, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")


##################################################################################


# Iterative Algorithm

def binarySearchItr(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        # Check if x is present at mid
        if arr[mid] < x:
            low = mid + 1

        # If x is greater, ignore left half
        elif arr[mid] > x:
            high = mid - 1

        # If x is smaller, ignore right half
        else:
            return mid

    # If we reach here, then the element was not present
    return -1


# Test array
arr = [200, 36, 4, 100, 40]
x = 100  # Output => 3

# Function call
result = binarySearchItr(arr, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
