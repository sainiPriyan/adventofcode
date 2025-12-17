input_data = []

with open('input.txt') as file:
    input_data = file.readlines()

count = 0
pointer = 50

for line in input_data:

    line = line.strip()
    num = int(line[1:])

    if line[0] == 'R':
        pointer = (pointer + num)%100

    elif line[0] == 'L':
        pointer = (pointer - num)%100

    if pointer == 0:
        count +=1    

    print(line)
    print(pointer)
    print(count)    
    print("-----")


print(count)            