from string import ascii_uppercase

with open('input_22', 'r') as f:
    fl = f.read()

fl = fl.replace('"', '')
name_list = fl.split(',')
name_list.sort()
prod = 0
for index, name in enumerate(name_list):
    prod += (index+1)*sum([ascii_uppercase.find(i)+1 for i in name])
print prod
