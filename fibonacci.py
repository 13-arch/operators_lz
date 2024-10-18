input_data = open('input.txt', 'r')
output = open('output.txt', 'w')
data = input_data.read()
data = data.split()
output.write(str('0, '))
a =int(data[0])
f1=0
f2=1
for i in range(1,a):
    output.write(str(f1+f2) +(', '))
    if i%2 ==0 :
        f1=f1+f2
    elif i%2==1:
        f2=f1+f2
output.write(str(f2+f1))      
input_data.close()
output.close()