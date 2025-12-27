import math
import heapq

def find_distance(a,b):
    return (a[1]-b[1])**2 + (a[2]-b[2])**2 + ((a[0]-b[0])**2 )


with open('D:\\Projects\\adventofcode\\2025\\day8\\input.txt') as file:
    lines = file.read().splitlines()

input_data = [ list(map(int,line.split(',')) ) for line in lines]    

# print(input_data)

distance = {}

for i in range(len(input_data)-1):
    for j in range(i+1, len(input_data)):
        distance[(i,j)] = find_distance(input_data[i],input_data[j])

# print(distance)
sorted_distance = heapq.nsmallest(1000, distance.items(), key=lambda x: x[1])

# print('\nSorted Dist:')
# print(sorted_distance)

final  = []



for k,v in sorted_distance:
    a = -1
    b = -1

    for i,s in enumerate(final):
        if k[0] in s:
            a = i
            
        if k[1] in s:
             b = i
             
    if a == -1 and b == -1:
        final.append({k[0], k[1]})
    elif a != -1 and b == -1:
        final[a].add(k[1])
    elif a == -1 and b != -1:
        final[b].add(k[0])
    elif a != b:
        hi, lo = max(a, b), min(a, b)
        final[lo].update(final[hi])
        final.pop(hi)

#     print(f'on {k[0],k[1]} appending: {final}')  
            
# print(f'final list: {final}')   

x = 0
y = 0
z = 0

for i in final:
    length = len(i)

    if(length > x):
        z = y
        y = x
        x = length
    
    elif(length > y):
        z = y
        y = length

    elif length > z:
        z = length

print(f'x = {x}, y = {y}, z = {z}')

print (x*y*z)