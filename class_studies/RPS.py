def main():
    player1 = input()
    player2 = input()

    C2N = {'paper': 0,
           'rock': 1,
           'scissors': 2}
    player1 = C2N[player1]
    player2 = C2N[player2]
    results = [
        ['tie', 'player 1 wins', 'player 2 wins',],
        ['player 2 wins', 'tie', 'player 1 wins',],
        ['player 1 wins', 'player 2 wins', 'tie',],
    ]
    print(results[player1][player2])


main()
