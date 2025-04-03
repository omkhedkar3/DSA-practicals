class SetADT:
    def __init__(self):
        """Initialize the set (using a dictionary to store unique elements)."""
        self.elements = {}

    def add(self, element):
        """Add an element to the set."""
        self.elements[element] = None

    def remove(self, element):
        """Remove an element from the set if it exists."""
        if element in self.elements:
            del self.elements[element]
        else:
            raise KeyError(f"Element '{element}' not found in the set.")

    def contains(self, element):
        """Check if an element exists in the set."""
        return element in self.elements

    def size(self):
        """Return the number of elements in the set."""
        return len(self.elements)

    def __iter__(self):
        """Return an iterator for the set."""
        return iter(self.elements)

    def intersection(self, other_set):
        """Return the intersection of this set and another set."""
        result = SetADT()
        for element in self.elements:
            if other_set.contains(element):
                result.add(element)
        return result

    def union(self, other_set):
        """Return the union of this set and another set."""
        result = SetADT()
        for element in self.elements:
            result.add(element)
        for element in other_set:
            result.add(element)
        return result

    def difference(self, other_set):
        """Return the difference between this set and another set (elements in this set but not in the other)."""
        result = SetADT()
        for element in self.elements:
            if not other_set.contains(element):
                result.add(element)
        return result

    def subset(self, other_set):
        """Check if this set is a subset of another set."""
        for element in self.elements:
            if not other_set.contains(element):
                return False
        return True

# Example usage
if __name__ == "__main__":
    set1 = SetADT()
    set1.add(1)
    set1.add(2)
    set1.add(3)

    set2 = SetADT()
    set2.add(2)
    set2.add(3)
    set2.add(4)

    print("Set 1 contains 2:", set1.contains(2))  # True
    print("Set 1 size:", set1.size())             # 3

    set1.remove(2)
    print("Set 1 after removing 2:", [x for x in set1])  # [1, 3]

    # Union
    union_set = set1.union(set2)
    print("Union of Set 1 and Set 2:", [x for x in union_set])  # [1, 3, 2, 4]

    # Intersection
    intersection_set = set1.intersection(set2)
    print("Intersection of Set 1 and Set 2:", [x for x in intersection_set])  # [3]

    # Difference
    difference_set = set1.difference(set2)
    print("Difference of Set 1 and Set 2:", [x for x in difference_set])  # [1]

    # Subset check
    print("Is Set 1 a subset of Set 2?", set1.subset(set2))  # False
    print("Is Set 2 a subset of Set 1?", set2.subset(set1))  # False

