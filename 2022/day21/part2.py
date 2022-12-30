with open("input.txt", "r") as f:
    data = f.read()

lines = data.split('\n')

left = -10 ** 30
right = 10 ** 30
while True:
    mid = (left + right) // 2
    values = {'humn': mid}
    change = True
    while change:
        change = False
        for line in lines:
            monkey, remaining = line.split(': ')

            if monkey in values or monkey == 'root':
                continue
            
            if remaining.isnumeric():
                values[monkey] = int(remaining)
                change = True
            else:
                a, op, b = remaining.split()

                if a in values and b in values:
                    values[monkey] = eval(f'{values[a]} {op} {values[b]}')
                    change = True

    for line in lines:
        if line.startswith('root:'):
            root, a, op, b = line.split(' ')
            assert a in values and b in values

            if values[a] < values[b]:
                right = mid
            else:
                left = mid
            
            if values[a] == values[b]:
                print(mid)
                exit()
