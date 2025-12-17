input_data = []
sum = 0

with open('D:\\Projects\\adventofcode\\2025\\day2\\input.txt') as file:
    input_data = file.read().split(',')

print(input_data)    

for data in input_data:
    a,b = data.split('-')
    
    for i in range(int(a), int(b)+1):

        if(len(str(i)) == 1): 
            continue

        s = str(i)

        k = len(s)//2 
        
        for k in range(k, 0, -1):

            parts = [(s[j:j+k]) for j in range(0, len(s), k)]

            if len(set(parts)) == 1:
                sum += i
                break

print(sum)    
            