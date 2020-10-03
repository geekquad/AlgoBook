"""
bubble_sort.py is a simple implementation of the Bubble Sort algorithm. 
"""

def bubble_sort(unsorted_list: [int]) -> [int]:
    """Simple bubble sort implementation, which sorts a given list of integers by increasing size. 

    Args:
        unsorted_list ([int]): an array of integers.

    Returns:
        [int]: an array of integers, but now sorted by increasing size.
    """

    # Iterate through list x times, where x is length of unsorted_list.
    for i in range(len(unsorted_list)):
        for j in range(len(unsorted_list) - 1):
            # If previous element is larger, swap them.
            if unsorted_list[j] > unsorted_list[j+1]:
                unsorted_list[j], unsorted_list[j+1] = unsorted_list[j+1], unsorted_list[j]
    
    # Your list is sorted now!
    return unsorted_list
