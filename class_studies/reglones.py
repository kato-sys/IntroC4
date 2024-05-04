width, start, end = map(int, input().split(' '))

if start < end:
    for char in range(start, end + 1, 1):
        print(f'{char:>3} {'_'*width}')
else:
    for char in range(start, end - 1, -1):
        print(f'{char:>3} {'_'*width}')
