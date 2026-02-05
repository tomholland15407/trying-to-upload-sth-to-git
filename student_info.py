from shutil import copyfile
import pickle
copyfile('student_info.pkl', 'updated_info.pkl')
with open('student_info.pkl', 'rb') as f:
    data = pickle.load(f)
new_student = {
        'id': 20200000,
        'name': 'Nguyen Van Anh',
        'score': {
            'math': 7.8,
            'english': 8.4,
            'physics': 8.0,
        }
    }
def add_student_info(new_student):
    with open('updated_info.pkl', 'rb') as f:
        content = pickle.load(f)

    for index, student in enumerate(content):
        if student['id'] == new_student['id']:
            content[index] = new_student
            break
    with open('updated_info.pkl', 'wb') as f:
        pickle.dump(content, f)
add_student_info(new_student)
with open('updated_info.pkl', 'rb') as f:
    content = pickle.load(f)

print('Before:')
print('Number of students: ', len(data))
print('Name of student 0: ', data[0]['name'])
print('After:')
print('Number of students: ', len(content))
print('Name of student 0: ', content[0]['name'])