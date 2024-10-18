input_data = open('input.txt', 'r')
output = open('output.txt', 'w')
data = input_data.read()
data = data.split()
a = int(data[0])
for i in range(2, 25000):
    if a%i == 0 and i != a:
        output.write(str('N'))
        break
    elif i == a:
        output.write(str('Y'))
if a == 1:
    output.write(str('N'))      
input_data.close()
output.close()