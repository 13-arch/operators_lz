input_data = open('input.txt', 'r')
output = open('output.txt', 'w')
data = input_data.read()
a = int(data)#выводим число из файла input.txt
for i in range(2, 25000):#задаем промежуток
    if a%i == 0 and i != a:#задаем условие
        output.write(str('N'))
    elif i == a:
        output.write(str('Y'))
if a == 1:
    output.write(str('N'))
input_data.close()
output.close()