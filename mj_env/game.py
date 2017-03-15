from mj_env.player import Player
from mj_env.table import MahjongTable
from mj_env.checker import Checker
from mj_env.strategy import NNStrategy
import time
INIT_TILT_SIZE = 13
SUITE_SIZE = 108


def main():

    n_players = 2
    winner = -1 # 0 to 3
    players = [Player('Player', i, NNStrategy()) for i in range(n_players)]
    dealer_index = 0
    table = MahjongTable(players)

    table.get_ready(dealer_index)
    # start game
    if len(players) > 4 or len(players) <= 0:
        print("invalid number of players")
    # init
    else:
        for player in players:
            player.draw(table, INIT_TILT_SIZE)  # init
        i = dealer_index
        cnt = 0
        while table.has_next_tile():
            cnt += 1
            player_index = i%n_players  # todo: to be refactored when support gang peng
            print("Round:" + str(cnt))
            player = players[player_index]
            print("Player " + str(player.id))
            print(player.get_xiajiao())
            player.draw(table, 1)
            print(player.get_hand_tile().get_last())
            player.sort_private_tiles()
            if player.check_win():
                print("Hu le!")
                winner = player.id
                break
            tile = player.discard_tile(table)
            player.check_if_i_have_a_jiao()
            table.take_the_discarded_tile(player_index, tile)
            print(player.get_hand_tile())
            table.show_the_pool()
            print("***** END OF THIS PLAYER *******")
            time.sleep(1)
            i += 1

        print("**** WINNER IS ******: " + str(winner))

if __name__ == "__main__":
    main()
