import random

def partition(input_sequence, Left, Right):

            limit = input_sequence[Left]

            Less = Left + 1

            More = Less

            while More != Right:

                if input_sequence[ More ] < limit:

                    input_sequence[ Less ], input_sequence[ More ] = input_sequence[ More ], input_sequence[ Less ]

                    Less += 1

                More += 1

            pivot = Less - 1

            input_sequence[ Left ], input_sequence[ pivot ] = input_sequence[ pivot ], input_sequence[ Left ]

            return pivot

def partition3(input_sequence,Left, Right):

            part = partition( input_sequence, Left, Right )

            m1 = part

            m2 = part

            i = Right - 1

            while m2 < i:

                if input_sequence[ i ] == input_sequence[ part ]:

                    input_sequence[ m2 ], input_sequence[ i ] = input_sequence[ i ], input_sequence[ m2 ]

                    m2 += 1

                else:

                    i -= 1

            return m1, m2

       

def randomized_quick_sort(input_sequence, Left, Right ):

            if Right - Left < 2:

                return

            part = random.randint( Left, Right-1 )

            input_sequence[ Left ], input_sequence[ part ] = input_sequence[ part ], input_sequence[ Left ]

            m1, m2 = partition3( input_sequence, Left, Right )

            randomized_quick_sort( input_sequence, Left, m1 )

            randomized_quick_sort( input_sequence, m2, Right )

if __name__ == '__main__':

        no_of_inputs = input('Enter no. of inputs')

        input_sequence= list( map( int, input('Enter numbers to be sort separated by one spacing').split() ))

        Left = 0

        Right = len(input_sequence)    

        randomized_quick_sort( input_sequence , Left , Right )

        for x in input_sequence:

            print( x, end=" " )
