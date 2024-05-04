import sys

all_nums = []

for num in sys.stdin:
    all_nums.append(float(num))

print(f'Máximo: {max(all_nums):.2f}')
print(f'Mínimo: {min(all_nums):.2f}')
print(f'Media: {sum(all_nums)/len(all_nums):.2f}')
