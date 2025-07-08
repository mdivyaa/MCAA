# Array Operations
n = int(input("Enter the number of elements in array: "))
arr = []

# Input array elements
print("Enter", n, "elements:")
for i in range(n):
    arr.append(int(input()))

# A. Max and Min
max_val = max(arr)
min_val = min(arr)

# B. Total and Average
total = sum(arr)
average = total / len(arr)

# C. Remove Duplicates
unique = list(set(arr))

# Display results
print("\nOriginal Array:", arr)
print("Maximum:", max_val)
print("Minimum:", min_val)
print("Total:", total)
print("Average:", average)
print("Without Duplicates:", unique)
