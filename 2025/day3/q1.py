input_data = []
sum = 0

largest = -1
second_largest = -1

with open('D:\\Projects\\adventofcode\\2025\\day3\\input.txt') as file:
    input_data = file.read().splitlines()

# print(input_data)    
        
for line in input_data:

    for i in range(len(line) - 1):
        if  (int(line[i])>largest):
            second_largest = int(line[i+1])
            largest = int(line[i])

        elif (int(line[i])>second_largest):
            second_largest = int(line[i])

    last = int(line[len(line)-1])

    if(last > second_largest):
        second_largest = last

    num = str(largest) + str(second_largest)

    print(num)
    sum += int(num)
    print(f"sum: {sum}")

    largest = -1
    second_largest = -1    