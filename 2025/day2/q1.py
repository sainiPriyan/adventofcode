input_data = []
sum = 0

with open('D:\\Projects\\adventofcode\\2025\\day2\\input.txt') as file:
    input_data = file.read().split(',')

print(input_data)    

for data in input_data:
    a,b = data.split('-')
    
    for i in range(int(a), int(b)+1):
        if len(str(i))%2 != 0:
            continue

        left = str(i)[:len(str(i))//2] 
        right = str(i)[len(str(i))//2:]

        print(f'left: {left}, right: {right}')

        if(left==right):
            sum += i
            print('yes')


    print('---')

print(sum)    
            