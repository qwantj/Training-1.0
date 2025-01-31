with open('input.txt', 'r') as file:
    a, b = map(int, file.readline().split())
    c = file.readline().strip()

if c == 'auto':
    res = b
elif c == 'freeze':
    if a > b:
        res = b
    else:
        res = a
elif c == 'heat':
    if a < b:
        res = b
    else:
        res = a
else:
    res = a

with open('output.txt', 'w') as file:
    file.write(str(res))