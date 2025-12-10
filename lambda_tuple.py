tuple_list = [(-3, 4, 9), (5, 6, 7), (10, 16, 70), (1, 6, -7)]
query = (1, 2, 5)
k = 3

def closest_tuple(tuple_list, query, k):
    return min(tuple_list, key=lambda x: abs(x[k-1] - query[k-1]))

print(closest_tuple(tuple_list, query, k))
