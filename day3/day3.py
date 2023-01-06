file = open("data.txt")

lines = file.readlines()

dups = []
for sack in lines: 
    items = []
    length = len(sack) // 2
    first, second = set(sack[length:]), set(sack[:length])
    
    for item in first:
        if item in second:
            dups.append(item)

# can write function that return the 1-26 and 27-52 for alphabets to avoid the below maps
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
    check = set(words[0])
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

