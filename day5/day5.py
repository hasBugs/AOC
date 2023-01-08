def getData():
    file = open("data.txt")

    lines = file.readlines()
    stacks = [[] for x in range(9)]

    for line in lines[7::-1]:
        col = 0
        for num in range(1,35, 4):
            if(line[num].strip() != ''):
                stacks[col].append((line[num]))
            col+=1
    return [lines, stacks] 

def part1():
    lines, stacks = getData()
    for line in lines[10:]:
        num, frm, to = [int(x.strip()) for x in line.split(' ')[1::2]]
        
        for times in range(num):
            if stacks[frm-1]:
                stacks[to-1].append(stacks[frm-1].pop())
    printTops(stacks)

def part2():
    lines, stacks = getData()
    for line in lines[10:]:
        num, frm, to = [int(x.strip()) for x in line.split(' ')[1::2]]

        temp = stacks[frm-1][len(stacks[frm-1])-num:]
        stacks[frm-1] = stacks[frm-1][:len(stacks[frm-1])-num] 
        stacks[to-1] = stacks[to-1] + temp
    printTops(stacks)


def printTops(stacks):
    print(''.join([x[-1] for x in stacks]))

part1()
part2()
