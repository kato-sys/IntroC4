import sys

nod = int(input())
all_nums = []

if nod == 0:
    print('')
else:
    for num in sys.stdin:
        all_nums.append(int(num))
    print(sum(all_nums)/len(all_nums))
