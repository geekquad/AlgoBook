def cycle_sort(num_list):
    "Sort a list in place and return the number of writes."
    writes = 0
 
    # Loop through the list to find cycles to rotate.
    for list_start, item in enumerate(num_list):
 
        # Find where to put the item.
        pos = list_start
        for item2 in num_list[list_start + 1:]:
            if item2 < item:
                pos += 1
 
        # If the item is already there, this is not a loop.
        if pos == list_start:
            continue
 
        # Otherwise, put the item there or right after any duplicates.
        while item == num_list[pos]:
            pos += 1
        num_list[pos], item = item, num_list[pos]
        writes += 1
 
        # Rotate the rest of the loop.
        while pos != list_start:
 
            # Find where to put the item.
            pos = list_start
            for item2 in num_list[list_start + 1:]:
                if item2 < item:
                    pos += 1
 
            # Put the item there or right after any duplicates.
            while item == num_list[pos]:
                pos += 1
            num_list[pos], item = item, num_list[pos]
            writes += 1
 
    return writes
 
 
num_list = [75, 16, 55, 19, 48, 14, 2, 61, 22, 100]
print("Before: ", num_list)
cycle_sort(num_list)
print("After:  ", num_list)
