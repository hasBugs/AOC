file = open("data.txt")

lines = [line.strip().split(',') for line in file.readlines()]

count = 0
count2 = 0
for line in lines:
    s1, e1 = [int(x) for x in line[0].split('-')] 
    s2, e2 = [int(x) for x in line[1].split('-')] 

    
    if (s1 >= s2 and e1 <= e2) or (s2 >= s1 and e2 <= e1):
        count+=1

    # if s1 >= s2 and s1 <= e2:
    #     count2+=1
    # elif e1 >= s2 and e1 <= e2:
    #     count2+=1
    # elif s2 >= s1 and s2 <= e1:
    #     count2+=1
    # elif e2 >= s1 and e2 <= e1:
    #     count2+=1

    # simplified
    if not (e1 < s2 or e2 < s1):
        count2 +=1   

print(count)
print(count2)
