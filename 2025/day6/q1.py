input_data = [[]]

final_sum = 0

with open('D:\\Projects\\adventofcode\\2025\\day6\\input.txt') as file:
    lines = file.read().splitlines()

input_data = [line.strip().split() for line in lines]

for row in input_data:
    for i in range(len(row)):
        if row[i] == '*' or row[i] == '+':
            continue
        else:    
            row[i] = int(row[i])


# print(input_data)


for i in range(len(input_data[0])):
    
    if input_data[len(input_data)-1][i] == '*':
        sum = 1
        for j in range(len(input_data) - 1):
            sum *= input_data[j][i]

        # print(f'product = {sum}')    
    else :
        sum = 0
        for j in range(len(input_data) - 1):
            sum += input_data[j][i]    

        # print(f'sum = {sum}')    

    final_sum += sum              

print(f'final sum = {final_sum}')