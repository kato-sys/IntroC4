width, start, end = map(int, input().split(' '))

space = max(len(str(start)), len(str(end)))

step = +1 if start < end else -1

for char in range(start, end + step, step):
    print(f"{char:{space}} {'_'*width}")
