with open('./data/prueba.txt') as file:
    file_data = file.readlines()
    
file_data_list = []

for word in file_data:
    for letter in word:
        if letter != '\n' and letter != '0' and letter != '1' and letter != '2' and letter != '3' and letter != '4' and letter != '5' and letter != '6'and letter != '7' and letter != '8' and letter != '9':
            file_data_list.append(letter)

# print(file_data_list)

prueba = ''

for i in range(len(file_data_list)):
    if file_data_list[i] != ' ':
        prueba += file_data_list[i]
    elif file_data_list[i] == ' ':
        prueba += '\n'
        
with open("english.txt", "a") as data_file:
    data_file.write(prueba)
    
print(prueba)
