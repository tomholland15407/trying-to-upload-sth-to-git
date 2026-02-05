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
dictionary = {}
running = True
while running:
    pair = input().split(' ')
    if pair[0] == '***':
        running = False
    else:
        dictionary[pair[0]] = pair[1]
ancestor = [parent for child, parent in dictionary.items() if parent not in dictionary.keys()]
def generation(name):
    if name == ancestor[0]:
        return 1
    elif dictionary[name] == ancestor[0]:
        return 2
    else:
        return 1 + generation(dictionary[name])
reversed_dict = {}
for key, value in dictionary.items():
    reversed_dict.setdefault(value, []).append(key)

def descendant(name):
    if name not in reversed_dict.keys():
        return 0
    else:
        direct = len(reversed_dict[name])
        for child in reversed_dict[name]:
            if child in reversed_dict.keys():
                direct += descendant(child)
        return direct

going = True
while going:
    code = input().split(' ')
    if code[0] == '***':
        going = False
    else:
        cmd = code[0]
        para = code[1]
        if cmd == 'descendants':
            print(descendant(para))
        elif cmd == 'generation':
            print(generation(para))

