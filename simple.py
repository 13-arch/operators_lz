input_data = open('input.txt', 'r')
output = open('output.txt', 'w')
data = input_data.read()
data = data.split()#разделение элементов
a = int(data[0])#вводим значение 
for i in range(2, a):#цикл
    if a%i == 0 and i != a:#условие
        output.write(str('N'))
        break#прерываем цикл
    elif i == a:#условие
        output.write(str('Y'))
if a == 1:#условие
    output.write(str('N'))      
input_data.close()
output.close()