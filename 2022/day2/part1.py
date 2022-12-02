

data = open("input.txt").read()

score = 0
for l in data.split("\n"):
    opp, you = l.split()

    if you == "X":
        if opp == "C":
            score += 6
        if opp == "A":
            score += 3
        score += 1

    if you == "Y":
        if opp == "A":
            score += 6
        if opp == "B":
            score += 3
        score += 2

    if you =="Z":
        if opp == "B":
            score += 6
        if opp == "C":
            score += 3
        score += 3

print(score)