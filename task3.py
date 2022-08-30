files_dict = {}

with open('1.txt','r', encoding='utf-8') as file:
    count1 = 0
    for line in file:
        count1 += 1
files_dict['1.txt'] = count1

with open('2.txt','r', encoding='utf-8') as file:
    count2 = 0
    for line in file:
        count2 += 1
files_dict['2.txt'] = count2

with open('3.txt','r', encoding='utf-8') as file:
    count3 = 0
    for line in file:
        count3 += 1
files_dict['3.txt'] = count3

print(files_dict)
list_value = []
for key, value in files_dict.items():
    list_value.append(value)
list_value.sort()

list_file_names = []
for element in list_value:
    for key, value in files_dict.items():
        if value == element:
            list_file_names.append(key)

with open('final.txt','w', encoding='utf-8') as file_final: 
    file_final.write('\n')

for i in range(3):
    with open('final.txt','a', encoding='utf-8') as file_final:    
        with open(list_file_names[i],'r', encoding='utf-8') as file:
            file_final.write(list_file_names[i]+'\n')
            file_final.write(str(list_value[i])+'\n')
            for line in file:
                file_final.write(line)
            file_final.write('\n')
