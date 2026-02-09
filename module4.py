# Read N (positive integer)
N = int(input("Enter N (positive integer): "))

# Read N numbers one by one
nums = []
for i in range(N):
    nums.append(int(input(f"Enter number {i+1}: ")))

# Read X (integer)
X = int(input("Enter X (integer to search for): "))

# Find and print 1-based index of X, or -1 if not found
if X in nums:
    print(nums.index(X) + 1)  # index() returns 0-based; add 1 for 1-based
else:
    print(-1)
