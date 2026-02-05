def sort_students(l):
    score_list = sorted(l, key=lambda x: (x[1], x[0]))

    return score_list
