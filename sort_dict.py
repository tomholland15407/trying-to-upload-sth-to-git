grades = {'a': 92, 'b': 92, 'c': 95}


sorted_dict = dict(sorted(grades.items(), key = lambda item: (-item[1],item[0])))

print(sorted_dict)