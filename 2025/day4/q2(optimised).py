from collections import deque

input_data = []

queue = deque()

with open('D:\\Projects\\adventofcode\\2025\\day4\\input.txt') as file:
    input_data = file.read().splitlines()

previous_accessible = 0
accessible = 0

neighbours = [[]]

neighbours = [[-1]*len(input_data[0]) for _ in range(len(input_data))]

for i in range(len(input_data)):
    for j in range(len(input_data[i])):
        if input_data[i][j] != '@':
            continue
        count = 0
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if di == 0 and dj == 0:
                    continue
                ni, nj = i + di, j + dj
                if 0 <= ni < len(input_data) and 0 <= nj < len(input_data[i]) and (input_data[ni][nj] == '@' or input_data[ni][nj] == 'q'):
                    count += 1
        neighbours[i][j] = count

        if count < 4:
            queue.append((i, j))
            input_data[i] = input_data[i][:j] + 'q' + input_data[i][j+1:]

# print(queue)            


while len(queue) > 0:
    cur = queue.popleft()
    accessible += 1

    cur_i, cur_j = cur

    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if di == 0 and dj == 0:
                continue
            ni, nj = cur_i + di, cur_j + dj
            if 0 <= ni < len(input_data) and 0 <= nj < len(input_data[ni]) and input_data[ni][nj] == '@':
                neighbours[ni][nj] -= 1
                if neighbours[ni][nj] < 4:
                    queue.append((ni, nj))
                    input_data[ni] = input_data[ni][:nj] + 'q' + input_data[ni][nj+1:]

print(f'Accessible positions: {accessible}')


