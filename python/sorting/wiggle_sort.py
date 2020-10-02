'''Wiggle Sort Algorithm'''


def wiggle_sort(wiggle_list):

    '''
    # Input Arguments:
    #     wiggle_list --> an unordered list of integers
    # Output:
    #     wiggle_list --> the input list that has been sorted in place such that even-indexed elements
    #                     are less than or equal to their neighboring odd-indexed elements
    #                     --> output represents one of many possible solutions
    '''

    '''
    # ***Input/Output Examples***
    #
    # In  --> []
    # Out --> []
    #
    # In  --> [2, 1]
    # Out --> [1, 2]
    #
    # In  --> [2, 1, 4, 3, 6, 5]
    # Out --> [1, 4, 2, 6, 3, 5]
    #
    # In  --> [1, -1, 1, -1, 1, -1, 1]
    # Out --> [-1, 1, -1, 1, -1, 1, 1]
    #
    # In  --> [7, 1, 11, 2, 12, 3, 13]
    # Out --> [1, 11, 2, 12, 3, 13, 7]
    '''


    """ Iterating starting at the second index location (i=1) to the end of the list """
    for i in range(1, len(wiggle_list)):

        """Testing if list is empty or only one element in length"""
        if not wiggle_list or len(wiggle_list) <= 1:
            return wiggle_list

        """Testing if current iterator step in an odd or even index location"""
        if i%2==1:

            """Testing if the current odd-index element is smaller than the previous
               even-index element and swapping the elements if so"""
            if wiggle_list[i-1] > wiggle_list[i]:
                wiggle_list[i-1], wiggle_list[i] = wiggle_list[i], wiggle_list[i-1]

        else:

            """Testing if the current even-index element is larger than the previous
               odd-index element and swapping the elements if so"""
            if wiggle_list[i-1] < wiggle_list[i]:
                wiggle_list[i-1], wiggle_list[i] = wiggle_list[i], wiggle_list[i-1]

    return wiggle_list



#Process Driver Code

if __name__ == '__main__':
    
    input_list = input("Enter a list of integers separated by commas : ")
    int_list = [int(num) for num in input_list.split(",") if num]
    print("Original List:      ", int_list)

    wiggle_sorted_list = wiggle_sort(int_list)
    print("Wiggle Sorted List: ", wiggle_sorted_list)
    
