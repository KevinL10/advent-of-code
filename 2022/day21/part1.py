with open("input.txt", "r") as f:
    data = f.read()

values = {}
change = True
while change:
    change = False
    for line in data.split('\n'):
        monkey, remaining = line.split(': ')

        if monkey in values:
            continue
        
        if remaining.isnumeric():
            values[monkey] = int(remaining)
            change = True
        else:
            a, op, b = remaining.split()
            if a in values and b in values:
                values[monkey] = eval(f'{values[a]} {op} {values[b]}')
                change = True

print(int(values['root']))