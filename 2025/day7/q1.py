from collections import deque

count = 0

class TreeNode:
    def __init__(self, data):
        self.i= data[0]
        self.j = data[1]

        self.right = None
        self.left = None


with open('D:\\Projects\\adventofcode\\2025\\day7\\input.txt') as file:
    lines = file.read().splitlines()
    

lines = [list(row) for row in lines]    
# print(lines)

for j in range(len(lines[0])-1):
    if lines[0][j] == 'S':
        root = TreeNode((0, j))
        # print(root.i, root.j)
        break

queue = deque()
queue.append(root)   

while len(queue) > 0:

    node = queue[0]
    i = node.i
    j = node.j

    queue[0].i+=1
    i+=1

    # print(f'Visiting node at {i},{j}')

    if i >= len(lines):
        queue.popleft()
        continue

    if lines[i][j] == '.':
        # print(f'Found . at {i},{j}')
        lines[i][j] = '|'
        # print(lines[i])

    elif lines[i][j] == '^':

        # print(f'Found ^ at {i},{j}')

        queue.popleft()

        count += 1

        if j + 1 < len(lines[0]):
            lines[i][j+1] = '|'
            new_node = TreeNode((i, j+1))
            queue.append(new_node)
            
            
        if j - 1 >= 0:
            lines[i][j-1] = '|'
            new_node = TreeNode((i, j-1))
            queue.append(new_node)

        # print(lines[i])    

    elif lines[i][j] == '|':
        queue.popleft()        

print(f'count is {count}')