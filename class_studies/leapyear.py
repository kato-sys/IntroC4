line = int(input())
if line % 4 == 0 and line % 400 == 0:
    print(f'{line}: leap year')
else:
    print(f'{line}: normal year')
