file = open("data.txt")

lines = file.readlines()

values_map = {"A": 1, "B": 2, "C": 3}
conversion_map = {"X":"A", "Y":"B", "Z":"C"}

def getOutcome(opp, me):
    if(opp == conversion_map.get(me)):
        return values_map.get(conversion_map.get(me)) + 3
    elif(opp == "A" and conversion_map.get(me) == "B"):
        return values_map.get(conversion_map.get(me)) + 6
    elif(opp == "A" and conversion_map.get(me) == "C"):
        return values_map.get(conversion_map.get(me)) + 0
    elif(opp == "B" and conversion_map.get(me) == "A"):
        return values_map.get(conversion_map.get(me)) + 0
    elif(opp == "B" and conversion_map.get(me) == "C"):
        return values_map.get(conversion_map.get(me)) + 6
    elif(opp == "C" and conversion_map.get(me) == "A"):
        return values_map.get(conversion_map.get(me)) + 6
    elif(opp == "C" and conversion_map.get(me) == "B"):
        return values_map.get(conversion_map.get(me)) + 0

score = 0
for line in lines:
    spl = line.split(' ')
    score += getOutcome(spl[0], spl[1].strip())

print(score)

def getOutcome2(opp, me):
    if(opp == "A" and  me == "X"):
        return values_map.get("C") + 0
    elif(opp == "A" and me == "Y"):
        return values_map.get("A") + 3
    elif(opp == "A" and me == "Z"):
        return values_map.get("B") + 6
    elif(opp == "B" and  me == "X"):
        return values_map.get("A") + 0
    elif(opp == "B" and me == "Y"):
        return values_map.get("B") + 3
    elif(opp == "B" and me == "Z"):
        return values_map.get("C") + 6
    elif(opp == "C" and  me == "X"):
        return values_map.get("B") + 0
    elif(opp == "C" and me == "Y"):
        return values_map.get("C") + 3
    elif(opp == "C" and me == "Z"):
        return values_map.get("A") + 6    

score = 0
for line in lines:
    spl = line.split(' ')
    score += getOutcome2(spl[0], spl[1].strip())

print(score)