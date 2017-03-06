from mj_env.player import Player
from mj_env.table import MahjongTable
from random import randint
from mj_env.checker import Checker
import time
Init_Tile_Size = 13
Suite_Size = 108


def main():

    n_players = 2
    players = [Player('Player', i) for i in range(n_players)]
    dealer_index = 0
    table = MahjongTable(players, dealer_index)

    table.get_ready()
    # start game
    if len(players) > 4 or len(players) <= 0:
        print("invalid number of players")
    # init
    else:
        for player in players:
            player.draw(table, Init_Tile_Size)  # init
        i = dealer_index
        cnt = 0
        while table.get_bottom_size():
            cnt += 1
            print("Round:" + str(cnt))
            player = players[i%n_players]
            player.draw(table, 1)
            print("Player " + str(player.id))
            player.discard(randint(0,13), table)
            hand_tile = player.getHandTile()
            print(hand_tile)
            print(Checker.check_hu(hand_tile))
            table.show_the_pool()
            print("***** END OF THIS PLAYER *******")
            time.sleep(1)
            i += 1


if __name__ == "__main__":
    main()
