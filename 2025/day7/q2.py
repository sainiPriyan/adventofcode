from collections import defaultdict
count = 0
with open('D:\\Projects\\adventofcode\\2025\\day7\\input.txt') as file:
    lines = file.read().splitlines()
    

lines = [list(row) for row in lines]    
# print(lines)

for j in range(len(lines[0])-1):
    if lines[0][j] == 'S':
        root = (0,j)
        break

dict = defaultdict(int)
dict[(0, root[1])] = 1


for i in range(len(lines)):

    next = defaultdict(int)

    for (i,j), val in dict.items():

        new_i = i + 1

        if new_i >= len(lines):
            count += val
            continue

        if lines[new_i][j] == '.':
            next[new_i,j] += val

        else:
            if j>0 :
                next[new_i,j-1] += val
            if j+1 < len(lines[0]):
                next[new_i,j+1] += val

    dict = next                    

print(f'count is {count}')