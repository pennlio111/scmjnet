from mj_env.player import Player
from mj_env.table import MahjongTable
from random import randint
import time
Init_Tile_Size = 13

def main():
    n_players = 2
    players = [Player('player' + str(i), i) for i in range(n_players)]
    dealerIndex = 0
    table = MahjongTable(players, dealerIndex)

    table.getReady()
    # start game
    if len(players) > 4 or len(players) <= 0:
        print("invalid number of players")
    # init
    else:
        for player in players:
            player.draw(table, Init_Tile_Size)  # init
        i = dealerIndex
        while table.getBottomSize():
            player = players[i%n_players]
            player.draw(table, 1)
            print("Player " + str(player.id))
            print(player.getHandTile())
            player.discard(randint(0,13), table)
            print(player.getHandTile())
            table.showPool()
            time.sleep(1)
            i += 1
            print(table.getBottomSize())

if __name__ == "__main__":
    main()
