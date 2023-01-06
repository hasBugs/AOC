file = open("data.txt")

lines = file.readlines()

dups = []
for sack in lines: 
    items = []
    length = len(sack) // 2
    first, second = set(sack[length:]), set(sack[:length])
    
    for item in first:
        items.append(item)

    for item in second:
        if(item in items):
            dups.append(item)

lowercase = [chr(x+97) for x in range(26)]
uppercase = [chr(x+65) for x in range(26)]
numbers = [x+1 for x in range(52)]

alphabets = dict(zip(lowercase + uppercase, numbers))

score = 0
for item in dups:
    score += alphabets[item]

print(score)

# part 2
 
def commonChars(words):
    check = list(words[0])
    for word in words:
        newCheck = []
        for c in word:
            if c in check:
                newCheck.append(c)
                check.remove(c)
        check = newCheck
    
    return check

shared, squad = [], []
i = 0
for line in lines: 
    squad.append(line)
    if(len(squad) == 3):
        shared.append(commonChars(squad)[0])
        squad = []

score = 0
for item in shared:
    score += alphabets[item]

print(score)

