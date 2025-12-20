ranges = []
items = []

count = 0

with open('D:\\Projects\\adventofcode\\2025\\day5\\input.txt') as file:
    blocks = file.read().strip().split('\n\n')
    
ranges = [list(map(int, line.split('-'))) for line in blocks[0].splitlines()]

# print(f'Original ranges: {ranges}')

ranges = sorted(ranges, key=lambda x: x[0])

for i in range(0, len(ranges) - 1):
    if ranges[i][1] >= ranges[i + 1][0]:

        # print(f'Merging {ranges[i]} and {ranges[i + 1]}')

        ranges[i + 1][0] = ranges[i][0]
        ranges[i + 1][1] = max(ranges[i][1], ranges[i + 1][1])
        ranges[i] = None

        # print(f'New range: {ranges[i + 1]}')

# print(f'Merged ranges: {ranges}')


for r in ranges:
    if r is not None:
        count += r[1] - r[0] + 1

print(f'Count: {count}')        