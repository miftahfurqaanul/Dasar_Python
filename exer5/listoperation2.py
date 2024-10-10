list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

# Calculate element-wise sum and store in a new list
sum_list = []
for i in range(len(list1)):
    sum_list.append(list1[i] + list2[i])

# Print the original lists and the resulting list of sums
print("List 1:", list1)
print("List 2:", list2)
print("Sum List:", sum_list)

# Find and print the maximum element from each list
max_list1 = max(list1)
max_list2 = max(list2)
print("Maximum element in List 1:", max_list1)
print("Maximum element in List 2:", max_list2)