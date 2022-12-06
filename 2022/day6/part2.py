with open("input.txt", "r") as f:
    data = f.read()

for i in range(len(data)):
    if len(set(data[i:i+14])) == 14:
        print(i + 14)
        exit()