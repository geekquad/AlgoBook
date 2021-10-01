
class SegmentTree:
    """Non-recursive segment tree"""

    def __init__(self, items):
        """`items` is a list of numbers"""
        if type(items) is not list:
            raise TypeError("items must be a list")
        if not items:
            raise ValueError("items must have at least one value")

        self.items = items
        self._initialize_tree()


    def update(self, index, value):
        """Replaces item at `index` with `value`"""
        n = len(self.items)

        # Update the value itself
        tree[index + n] = value
        self._calculate_sums()

    def sum(self, left_index, right_index):
        """Returns the sum of values from `left_index` to `right_index` inclusive"""
        if right_index < left_index:
            raise ValueError("Right index must be higher than left index")

        # Shift indices to where they are in the tree (instead of self.items)
        # Also, bump right_index by one so that it's inclusive
        n = len(self.items)
        left_index += n
        right_index += n + 1

        # Loop through internal sums
        result = 0
        while left_index < right_index:
            if left_index & 1:
                result += self.tree[left_index]
                left_index += 1

            if right_index & 1:
                right_index -= 1;
                result += self.tree[right_index]

            left_index >>= 1
            right_index >>= 1
        return result

    def __str__(self):
        return str(self.tree)

    def __repr__(self):
        return f"<{self.__class__.__name__} items={self.items}, tree={self.tree}>"

    def _initialize_tree(self):
        """Initializes `self.tree` and calculates totals of leaf nodes"""
        # Initialize the tree
        n = len(self.items)
        self.tree = [0] * (2 * n)

        # Add original items
        for i in range(n):
            self.tree[n + i] = self.items[i]

        self._calculate_sums()

    def _calculate_sums(self):
        """Updates `self.tree[0...n-1]` with the leaf node sums"""
        n = len(self.items)
        # Calculate sums
        for i in range(n-1, 0, -1):
            left = self.tree[2 * i]
            right = self.tree[(2 * i) + 1]
            self.tree[i] = left + right

if __name__ == "__main__":
    # Test an even array
    a1 = [1, 2, 3, 4]
    t1 = SegmentTree(a1)
    assert t1.items == a1
    assert t1.tree == [0, 10, 3, 7, 1, 2, 3, 4]
    assert t1.sum(0, 3) == 10
    assert t1.sum(0, 0) == 1
    assert t1.sum(1, 2) == 5

    # Test an odd array
    a2 = [3, 5, 7, 9, 11]
    t2 = SegmentTree(a2)
    assert t2.items == a2
    assert t2.tree == [0, 35, 23, 12, 20, 3, 5, 7, 9, 11]
    t2.sum(0, 4) == 35
    t2.sum(0, 0) == 3
    t2.sum(4, 4) == 11
    t2.sum(1, 3) == 21