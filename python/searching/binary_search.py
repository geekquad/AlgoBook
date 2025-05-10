from typing import List, Optional

def binary_search(arr: List[int], target: int) -> Optional[int]:
    """
    Perform binary search on a sorted list of integers.

    Parameters:
    - arr (List[int]): Sorted list of integers.
    - target (int): The value to search for.

    Returns:
    - Optional[int]: Index of target if found, else None.
    """
    
    left = 0
    right = len(arr) - 1

    # Continue searching while the range is valid
    while left <= right:
        # Calculate the mid index to avoid integer overflow
        mid = left + (right - left) // 2

        # Debug: print current search range
        # print(f"Searching in range [{left}, {right}], mid={mid}")

        # If the middle element is the target, return its index
        if arr[mid] == target:
            return mid

        # If the middle element is less than target,
        # eliminate the left half (including mid)
        elif arr[mid] < target:
            left = mid + 1

        # If the middle element is greater than target,
        # eliminate the right half (including mid)
        else:
            right = mid - 1

    # Target was not found in the list
    return None
