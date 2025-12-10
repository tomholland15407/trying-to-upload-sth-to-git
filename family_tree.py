# Step-by-Step Plan
# - Read Input:
# - First line: number of people N.
# - Next N-1 lines: each line gives a child parent relationship.
# - Build Parent Map:
# - Create a dictionary: child → parent.
# - Find Ancestor:
# - The ancestor is the only person not listed as a child.
# - Compute Heights:
# - Use a dictionary heights = {ancestor: 0}.
# - For each person, recursively or iteratively compute their height by following their parent chain until you reach the ancestor.
# - Sort and Print:
# - Sort all names alphabetically.
# - Print each name followed by its height.

N = int(input())
dict = {}
for _ in range(N-1):
    pair = list(map(str, input().split()))
    dict[pair[0]] = pair[1]

ancestor = {parent for child, parent in dict.items() if parent not in dict.keys()}
print(ancestor)
