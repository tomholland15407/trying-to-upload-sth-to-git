def generate_partitions(n, max_num=None):
    if max_num is None:
        max_num = n
    if n == 0:
        return [[]]
    if n < 0 or max_num == 0:
        return []

    # Partitions that include max_num
    with_max = generate_partitions(n - max_num, max_num)
    with_max = [[max_num] + part for part in with_max]

    # Partitions that exclude max_num
    without_max = generate_partitions(n, max_num - 1)

    return with_max + without_max


# Example usage
partitions = generate_partitions(2)
for p in partitions:
    print(p)