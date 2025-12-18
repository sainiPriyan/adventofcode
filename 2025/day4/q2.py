input_data = []

with open('D:\\Projects\\adventofcode\\2025\\day4\\input.txt') as file:
    input_data = file.read().splitlines()

previous_accessible = 0
accessible = 0
# print(input_data)

while True:
    for i in range(len(input_data)):
        for j in range(len(input_data[i])):
            if input_data[i][j] != '@':
                continue
            up = 1 if i > 0 and input_data[i-1][j] == '@' else 0
            down = 1 if i < len(input_data)-1 and input_data[i+1][j] == '@' else 0
            left = 1 if j > 0 and input_data[i][j-1] == '@' else 0
            right = 1 if j < len(input_data[i])-1 and input_data[i][j+1] == '@' else 0
            top_left = 1 if i > 0 and j > 0 and input_data[i-1][j-1] == '@' else 0
            top_right = 1 if i > 0 and j < len(input_data[i])-1 and input_data[i-1][j+1] == '@' else 0
            bottom_left = 1 if i < len(input_data)-1 and j > 0 and input_data[i+1][j-1] == '@' else 0
            bottom_right = 1 if i < len(input_data)-1 and j < len(input_data[i])-1 and input_data[i+1][j+1] == '@' else 0

            if up + down + left + right + top_left + top_right + bottom_left + bottom_right < 4:
                input_data[i] = input_data[i][:j] + 'x' + input_data[i][j+1:]
                accessible += 1

    if accessible == 0:
        break    

    previous_accessible += accessible
    accessible = 0    

print(f'Accessible positions: {previous_accessible}')            