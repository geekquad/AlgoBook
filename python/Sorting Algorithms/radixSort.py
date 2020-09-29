def radixSort(list_of_ints: list[int]) -> list[int]:
    """
    radixSort(range(15)) == sorted(range(15))
    True
    radixSort(reversed(range(15))) == sorted(range(15))
    True
    radixSort([1,100,10,1000]) == sorted([1,100,10,1000])
    True
    """
    RADIX = 10
    placement = 1
    max_digit = max(list_of_ints)
    while placement <= max_digit:
        # declare and initialize empty buckets
        buckets = [list() for _ in range(RADIX)]
        # split list_of_ints between the buckets
        for i in list_of_ints:
            tmp = int((i / placement) % RADIX)
            buckets[tmp].append(i)
        # put each buckets' contents into list_of_ints
        a = 0
        for b in range(RADIX):
            for i in buckets[b]:
                list_of_ints[a] = i
                a += 1
        # move to next
        placement *= RADIX
    return list_of_ints
