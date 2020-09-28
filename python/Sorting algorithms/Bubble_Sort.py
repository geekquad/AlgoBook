def bubble_sort(lst):
    """
    Bubble sort function
    :param lst: lst of unsorted integers
    """

    # Traverse through all list elements
    for i in range(len(lst)):

        # Last i elements are already in place
        for j in range(0, len(lst) - i - 1):

            # Traverse the list from 0 to size of lst - i - 1
            # Swap if the element found is greater than the next element
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


# Driver code to test above
if __name__ == '__main__':

    lst = [3, 2, 1, 5, 4]
    bubble_sort(lst)  # Calling bubble sort function

    print("Sorted list is: ", lst)
    
