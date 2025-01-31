with open('input.txt', 'r') as file:
    a = int(file.readline().strip())
    b = int(file.readline().strip())
    c = int(file.readline().strip())
if (a + b > c) and (a + c > b) and (b + c > a):
    res = 'YES'
else:
    res = 'NO'
with open('output.txt', 'w') as file:
    file.write(res)