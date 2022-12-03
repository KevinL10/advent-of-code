from string import ascii_lowercase, ascii_uppercase

with open("input.txt", "r") as f:
    data = f.read()

out = 0

for l in data.split("\n"):
    s1 = l[:len(l)//2]
    s2 = l[len(l)//2:]

    a = set(s1).intersection(set(s2))

    for x in a:
        if x in ascii_lowercase:
            out += ascii_lowercase.index(x) + 1
        elif x in ascii_uppercase:
            out += ascii_uppercase.index(x) + 27
    
print(out)