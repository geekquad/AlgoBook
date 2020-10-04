# Takes the user's input and removes the spaces
raw_input = str(input("Enter input for double sorting: "))
stri = list(raw_input.replace(' ',''))

# Creates a list called counts, where I will store counts for each letter of my string
# I chose to use a list over a dictionary since dictionaries don't retain order

counts = []

# I loop through each letter that exists in the string, but I want to be careful to
# use a set here so that my letters are unique and I'm not revisiting the same letter
# twice. Python sets are magical and amazing! I add to my counts list a tuple of:
# the number of letters in the string, and the letter itself like: (8: 'o')

for letter in set(stri):
    counts.append((stri.count(letter), letter))

# I now have a list, not sorted in any way. I can both sort by both the frequency and
# the letter at the same time.

double_sort = sorted(counts, key=lambda tup: (-tup[0], tup[1]))

# Now I've got a sorted list of tuples, and I can print out the second item (letter) of
# each tuple in order of frequency and then alphabetical

for i in range(0, len(double_sort)):
    print (double_sort[i][1])
