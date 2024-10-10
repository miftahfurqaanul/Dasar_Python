set1 = {"apple", "banana", "orange", "grape"}
set2 = {"banana", "grape", "kiwi", "mango"}

# Print the union of the two sets
union_set = set1.union(set2)
print("Union of the sets:", union_set)

# Check if one set is a subset of the other
is_subset = set1.issubset(set2)
print("Is set1 a subset of set2?", is_subset)

# Remove a specific element from one of the sets
set1.remove("orange")
print("Updated set1:", set1)