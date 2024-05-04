import sys

tie = 0
player1 = 0
player2 = 0
total = 0
possible = ['R', 'P', 'S']

for choice in sys.stdin.read().splitlines():
    choices = choice.split(' ')
    if len(choices) > 1:
        p1 = choices[0].upper()
        p2 = choices[1].upper()
        if p1 in possible:
            if p2 in possible:
                C2N = {'P': 0,
                       'R': 1,
                       'S': 2}
                p1 = C2N[p1]
                p2 = C2N[p2]
                results = [
                    [0, 1, 2,],
                    [2, 0, 1,],
                    [1, 2, 0,],
                ]

                if results[p1][p2] == 0:
                    tie += 1
                    total += 1
                elif results[p1][p2] == 1:
                    player1 += 1
                    total += 1
                else:
                    player2 += 1
                    total += 1
            else:
                print(f'invalid shape: {p2}')
        else:
            print(f'invalid shape: {p1}')
    else:
        pass

if total == 0:
    print(f'Player1: {0:>3}{0:4}%')
    print(f'Player2: {0:>3}{0:>4}%')
    print(f'  Draws: {0:>3}{0:>4}%')
    print(f'  Total: {0:>3}{0:>4}% \n')
    print('   Draw!')
else:
    p1p = round((player1 * 100)/total)
    p2p = round((player2*100)/total)
    dp = round((tie*100)/total)
    tp = round((total*100)/total)
    print(f'Player1: {player1:>3}{p1p:>4}%')
    print(f'Player2: {player2:>3}{p2p:>4}%')
    print(f'  Draws: {tie:>3}{dp:>4}%')
    print(f'  Total: {total:>3}{tp:>4}% \n')
    if player1 > player2:
        print(' Winner: Player1')
    elif player2 > player1:
        print(' Winner: Player2')
    else:
        print('   Draw!')
