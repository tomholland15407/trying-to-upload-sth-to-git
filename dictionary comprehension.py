students = [
    {'id':1, 'name':'Alice', 'grade':92, 'class':'A'},
    {'id':2, 'name':'Bob', 'grade':85, 'class':'B'},
    {'id':3, 'name':'Charlie', 'grade':92, 'class':'A'}
]

class_dict = []
for dict in students:
    class_dict.append(dict['name'])
print(class_dict, 'number of students: ', len(class_dict))

unique_class=[s['class'] for s in students]
student_class={
    cl:[s['name'] for s in students if s['class']==cl]
    for cl in unique_class
}
print(student_class)

# Create dict: class -> list of students
# Create dict: grade -> count of students
# Create dict: name -> student (inverted index)