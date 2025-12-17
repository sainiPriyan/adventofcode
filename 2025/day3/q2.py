input_data = []
sum = 0

stack = []

with open('D:\\Projects\\adventofcode\\2025\\day3\\input.txt') as file:
    input_data = file.read().splitlines()

# print(input_data)    
        
for line in input_data:

    x = len(line) - 12
    
    for i in range(len(line)):
        curr = int(line[i])

        while len(stack) != 0 and curr > stack[-1] and x > 0:
            stack.pop()
            x -= 1

        stack.append(curr)    

    if x > 0:
        stack = stack[:-x]

    sum += int(''.join(map(str, stack)))
    # print(f"sum: {sum}")

    stack = []

print(f"Final sum: {sum}")
