opposite = {'NORTH': 'SOUTH',
            'EAST': 'WEST',
            'SOUTH': 'NORTH',
            'WEST': 'EAST'}


# Function to find the reduced
# direction
def dirReduc(givenDirections):
    finalDirections = []

    for d in range(0, len(givenDirections)):

        if finalDirections:

            if finalDirections[-1] == opposite[givenDirections[d]]:
                finalDirections.pop()
            else:
                finalDirections.append(givenDirections[d])

        else:
            finalDirections.append(givenDirections[d])

    return finalDirections


# Driver Code
print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))
