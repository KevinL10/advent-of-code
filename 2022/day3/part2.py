from string import ascii_lowercase, ascii_uppercase

with open("input.txt", "r") as f:
    data = f.read()

out = 0

data = data.split("\n")
for i in range(0, len(data), 3):
    shared = set(ascii_lowercase).union(set(ascii_uppercase))
    for j in range(i, i+3):
        shared = shared.intersection(set(data[j]))

    for x in shared:
        if x in ascii_lowercase:
            out += ascii_lowercase.index(x) + 1
        elif x in ascii_uppercase:
            out += ascii_uppercase.index(x) + 27
    
print(out)