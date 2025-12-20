ranges = []
items = []

count = 0

with open('D:\\Projects\\adventofcode\\2025\\day5\\input.txt') as file:
    blocks = file.read().strip().split('\n\n')
    
ranges = [list(map(int, line.split('-'))) for line in blocks[0].splitlines()]
items = blocks[1].splitlines()

# print(ranges)
# print(items)

for item in items:
    num = int(item)

    for r in ranges:
        if r[0] <= num <= r[1]:
            count += 1
            break
      
print(f'Count: {count}')
