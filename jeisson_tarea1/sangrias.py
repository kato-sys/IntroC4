import sys

print(input(), end='')
print('\n')

for line in sys.stdin:
    print('\t', line, end='\n')
