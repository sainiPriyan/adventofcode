input_data = [[]]

final_sum = 0

with open('D:\\Projects\\adventofcode\\2025\\day6\\input.txt') as file:
    lines = file.read().splitlines()
    print(lines)

operations = lines[len(lines) - 1].split()
print(operations)

operations_index = len(operations) - 1

sum = 0
product = 1

for j in range(len(lines[0])-1, -1,-1):

    s = ''

    for i in range(len(lines) - 1):
        c = lines[i][j]
        if c != ' ':
            s += c
    
    print(f's: {s}')

    if s == '':

        if operations[operations_index] == '+':
            final_sum += sum
            sum = 0
        elif operations[operations_index] == '*':
            final_sum += product
            product = 1

        operations_index -= 1
        continue

    if operations[operations_index] == '+':
        sum += int(s)
        print(f'sum: {sum}')
    elif operations[operations_index] == '*':
        product *= int(s)
        print(f'product: {product}')


final_sum += sum if operations[operations_index] == '+' else product        

print(f'final sum: {final_sum}')      
  