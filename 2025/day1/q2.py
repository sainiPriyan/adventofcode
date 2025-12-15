input_data = []

with open('input.txt') as file:
    input_data = file.readlines()

count = 0
pointer = 50

for line in input_data:

    line = line.strip()
    num = int(line[1:])

    if line[0] == 'R':
        if(pointer + num) >= 100:
            count += (pointer + num) // 100
        pointer = (pointer + num)%100    

    elif line[0] == 'L':
        if pointer == 0:
            pointer = 100
        
        count += num//100
        num = num % 100

        if(pointer - num) <= 0:
            count+=1
            
        pointer = (pointer - num)%100
  

    print(line)
    print(pointer)
    print(count)    
    print("-----")


print(count)            