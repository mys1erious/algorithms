import random as rnd


'''
1. Each player gives a gift once
2. Each player receives a gift once
3. Cant give/receive themselves
4. Random selection

Fred -> Wilma
Wilma -> Barney
Barney -> Pebbles
Pebbles -> BamBam
BamBam -> Fred
'''


# T: average: O(n); M: O(3n)
# Optimize to at least M: O(1) ?
def pair_players(players):
    gifters = [player for player in players]
    receivers = [player for player in players]
    res_map = {}

    while gifters:
        gifter = rnd.choice(gifters)
        receiver = rnd.choice(receivers)
        while receiver == gifter:
            receiver = rnd.choice(receivers)

        res_map[gifter] = receiver

        gifters.remove(gifter)
        receivers.remove(receiver)

    return res_map


if __name__ == '__main__':
    players = [
        'Fred',
        'Wilma',
        'Barney',
        'Pebbles',
        'BamBam'
    ]

    santas = pair_players(players)
    print(santas.keys())
    print(santas.values())
