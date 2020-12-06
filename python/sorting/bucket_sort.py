def bucket_sort(items, num_buckets=10):
    """
    Returns a sorted list of `items`, where each value in `items` is a value
    in [0.0, 1.0)
    """
    # Create list of buckets, where each bucket is a list
    buckets = []
    for _ in range(num_buckets):
        buckets.append([])

    # Add each item to its proper bucket
    for item in items:
        index = int(item * num_buckets)
        buckets[index].append(item)

    # Sort individual buckets
    for arr in buckets:
        merge_sort(arr)

    # Stitch buckets together
    return [item for bucket in buckets for item in bucket]

def merge_sort(items):
    """Sorts the list `items` in place"""

    if len(items) <= 1:
        return

    # Split list into two
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]

    # Sort each half individually
    merge_sort(left)
    merge_sort(right)

    # Sort the left and right lists together
    left_index = 0
    right_index = 0
    items_index = 0
    while (left_index < len(left)) and (right_index < len(right)):
        if left[left_index] < right[right_index]:
            next_item = left[left_index]
            left_index += 1
        else:
            next_item = right[right_index]
            right_index += 1

        items[items_index] = next_item
        items_index += 1

    # Add any remaining items
    while left_index < len(left):
        items[items_index] = left[left_index]
        left_index += 1
        items_index += 1
    while right_index < len(right):
        items[items_index] = right[right_index]
        right_index += 1
        items_index += 1


if __name__ == "__main__":
    # Test merge sort
    l1 = [1]
    merge_sort(l1)
    assert l1 == [1]

    l2 = [1, 2, 3, 4, 5]
    merge_sort(l2)
    assert l2 == [1, 2, 3, 4, 5]

    l3 = [4, 3, 2, 1]
    merge_sort(l3)
    assert l3 == [1, 2, 3, 4]


    l4 = [10, 40, 30, 15, 20, 34]
    merge_sort(l4)
    assert l4 == [10, 15, 20, 30, 34, 40]

    # Test bucket sort
    b1 = [0.5]
    assert bucket_sort(b1) == [0.5]

    b2 = [0.6, 0.4]
    assert bucket_sort(b2) == [0.4, 0.6]

    b3 = [0.9, 0.8, 0.85, 0.7]
    assert bucket_sort(b3) == [0.7, 0.8, 0.85, 0.9]

    b4 = [0.9, 0.6, 0.4, 0.5, 0.2, 0.3]
    assert bucket_sort(b4) == [0.2, 0.3, 0.4, 0.5, 0.6, 0.9]