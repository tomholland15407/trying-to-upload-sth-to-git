import re
with open('test_inp.txt', 'r') as file:
    content = file.read()
lst = re.findall(r'\S+\n?', content)
count = {}
for i in lst:
    count[i] = count.get(i, 0) + 1
with open('test_out.txt', 'w') as file:
    file.write(str(count))
with open('test_out.txt', 'r') as file:
    content = file.read()
print(content)