class Player:

    name = ''
    score = 0
    phase = 1

player1 = Player()
player2 = Player()
player3 = Player()
player4 = Player()
player5 = Player()
player6 = Player()

numPlayers = int(input('Enter the number of player (2-6): '))

players = [player1, player2]

if numPlayers >= 3:
    players.append(player3)
if numPlayers >= 4:
    players.append(player4)
if numPlayers >= 5:
    players.append(player5)
if numPlayers == 6:
    players.append(player6)


for x in range(0,numPlayers):
    currPlayer = players[x]

    currPlayer.name = input('Player {0} enter your name: '.format(x+1))

    print("Hello " + currPlayer.name)


    

