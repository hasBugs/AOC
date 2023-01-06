file = open("data.txt")

lines = [line.strip().split(',') for line in file.readlines()]

count = 0
count2 = 0
for line in lines:
    r1 = [int(x) for x in line[0].split('-')] 
    r2 = [int(x) for x in line[1].split('-')] 

    
    if (r1[0] >= r2[0] and r1[1] <= r2[1]) or (r2[0] >= r1[0] and r2[1] <= r1[1]):
        count+=1

    if r1[0] >= r2[0] and r1[0] <= r2[1]:
        count2+=1
    elif r1[1] >= r2[0] and r1[1] <= r2[1]:
        count2+=1
    elif r2[0] >= r1[0] and r2[0] <= r1[1]:
        count2+=1
    elif r2[1] >= r1[0] and r2[1] <= r1[1]:
        count2+=1

print(count)
print(count2)
