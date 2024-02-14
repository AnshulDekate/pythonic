from models import Board, Dice, Player

class Game:
    n_players = 0
    player_list = [] 
    curr_player = 0
    game_complete = 0
    def __init__(self, n_players, board_size, dice_size):
        self.n_players = n_players
        self.board = Board(board_size)
        self.dice = Dice(dice_size)
        for i in range(n_players):
            self.player_list.append(Player(i+1))
    
    def nxt_move(self):
        if self.game_complete:
            return 0

        player = self.player_list[self.curr_player]
        player.move(self.board, self.dice)
        if player.won:
            self.game_complete = 1
        
        self.curr_player = (self.curr_player+1)%self.n_players
        return 1
    
if __name__=="__main__":
    print("starting snake and ladder game")
    game = Game(3, 50, 6)
    while game.nxt_move():
        pass
    print("game completed")
    who_won = 0
    for player in game.player_list:
        if player.won==1:
            who_won = player.player_id
    print("Player {} won the game".format(who_won))
