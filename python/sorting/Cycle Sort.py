def cycle_sort(num_list):
    "Sort a list in place and return the number of writes."
    writes = 0
 
    for list_start, item in enumerate(num_list):
 
        pos = list_start
        for item2 in num_list[list_start + 1:]:
            if item2 < item:
                pos += 1

        if pos == list_start:
            continue
 
        while item == num_list[pos]:
            pos += 1
        num_list[pos], item = item, num_list[pos]
        writes += 1
 
        while pos != list_start:
 
            pos = list_start
            for item2 in num_list[list_start + 1:]:
                if item2 < item:
                    pos += 1
 
            while item == num_list[pos]:
                pos += 1
            num_list[pos], item = item, num_list[pos]
            writes += 1
 
    return writes
 
 
num_list = [75, 16, 55, 19, 48, 14, 2, 61, 22, 100]
print("Before: ", num_list)
cycle_sort(num_list)
print("After:  ", num_list)
