import re

col = """QGPRLCTF
JSFRWHQN
QMPWHBF
FDTSV
ZFVWDLQ
SLCZ
FDVMBZ
BJT
HPSLGBNQ"""

with open("input.txt", "r") as f:
    data = f.read()

out = 0

initial, instructions = data.split('\n\n')
crates = [list(l) for l in col.splitlines()]

for l in instructions.split('\n'):
    n, x, y = map(int, re.findall(r'\d+', l))
    x -= 1
    y -= 1
    tomove = crates[x][:n]
    crates[x] = crates[x][n:]
    crates[y] = tomove + crates[y]

ans = ""
for i in range(len(crates)):
    if len(crates[i]):
        ans += crates[i][0]

print(ans)