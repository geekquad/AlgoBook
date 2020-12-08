if __name__ == '__main__':
 
    # indicates the count of + or - at the top (+), bottom (-), left (+) and right (-) edges respectively.
    # value of -1 indicates any number of + or - signs
    top = [1, -1, -1, 2, 1, -1]
    bottom = [2, -1, -1, 2, -1, 3]
    left = [2, 3, -1, -1, -1]
    right = [-1, -1, -1, 1, -1]
 
    # rules matrix
    str = [
        ['L', 'R', 'L', 'R', 'T', 'T'],
        ['L', 'R', 'L', 'R', 'B', 'B'],
        ['T', 'T', 'T', 'T', 'L', 'R'],
        ['B', 'B', 'B', 'B', 'T', 'T'],
        ['L', 'R', 'L', 'R', 'B', 'B']
    ]
 
    (M, N) = (5, 6)